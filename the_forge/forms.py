from django import forms

class ContactDeveloperForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)