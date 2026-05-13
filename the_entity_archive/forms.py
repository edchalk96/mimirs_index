from .models import Entity
from django import forms

class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['name', 'featured_image', 'epithets', 'biography',]