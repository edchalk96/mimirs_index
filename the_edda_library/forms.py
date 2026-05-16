from .models import Lore, Entity
from .models import Comment
from django import forms
from django_select2 import forms as s2forms

class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = ['title', 'featured_image', 'content', 'entities', 'primary_source', 'notes',]
        widgets = {'entities': s2forms.Select2MultipleWidget(attrs={'data-placeholder': 'Leave blank or select entities...', 'data-allow-clear': 'true', 'style': 'width: 100%'})}

    def __init__(self, *args, **kwargs):
        super(LoreForm, self).__init__(*args, **kwargs)
        self.fields['entities'].required = False
        self.fields['entities'].queryset = Entity.objects.filter(status=1)

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)