from django.db import models
from django.contrib.auth.models import User
from the_entity_archive.models import Entity

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Lore(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    entities = models.ManyToManyField(Entity, related_name="appearances", blank=True)
    primary_source = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, related_name="user_lore_entries", on_delete=models.PROTECT)