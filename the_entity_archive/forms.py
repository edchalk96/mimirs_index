from .models import Entity
from django import forms


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['name', 'featured_image', 'epithets', 'biography', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['epithets'].help_text = "Separate each epithet with a comma."
