from django.db import models
from django.contrib.auth.models import User
from the_entity_archive.models import Entity
from django.utils.text import Truncator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Lore(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    entities = models.ManyToManyField(Entity, related_name="appearances", blank=True)
    excerpt = models.TextField(editable=False, blank=True)
    primary_source = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, related_name="user_lore_entries", on_delete=models.PROTECT)
    is_deletion_pending = models.BooleanField(default=False)
    featured_image = CloudinaryField('image', default='placeholder')

    def save(self, *args, **kwargs):
        if self.content:
            self.excerpt = Truncator(self.content).words(30, html=True)
        else:
            self.excerpt = ""

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} from {self.primary_source} {'PENDING DELETION' if self.is_deletion_pending else ''}"

class Comment(models.Model):
    lore = models.ForeignKey(Lore, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    # Credit to Tom Dekan for for parent field in creating comments thread - https://tomdekan.com/articles/comment-threads 
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.lore.title}"