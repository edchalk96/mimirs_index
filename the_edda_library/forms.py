from .models import Lore
from .models import Comment
from django import forms

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'content', 'entities', 'primary_source', 'notes',]

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)