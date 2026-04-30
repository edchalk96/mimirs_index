from django.shortcuts import render
from django.views import generic
# from .models import Entity

# Create your views here.
class ArchiveView(generic.TemplateView):
    template_name = "the_entity_archive/the_entity_archive.html"
