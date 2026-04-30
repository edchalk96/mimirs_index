from django.shortcuts import render
from django.views import generic

# Create your views here.
class ForgeView(generic.TemplateView):
    template_name = "the_forge/the_forge.html"