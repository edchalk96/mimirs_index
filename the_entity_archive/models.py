from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Entity(models.Model):
    entity_name = models.CharField(max_length=20, unique=True)
    epithets = ArrayField(models.CharField(max_length=20), blank=True)
    biography = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, related_name="user_entity_entries", on_delete=models.PROTECT)

    class Meta:
        ordering = ['entity_name']

    # Credit to Real Python for explanation and use of the @property decorator - https://realpython.com/python-property/
    @property
    def lore_count(self):
        return self.appearances.count()

    def __str__(self):
        return self.entity_name
