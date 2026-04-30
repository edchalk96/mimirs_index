from django.shortcuts import render
from django.views import generic
# from .models import Lore, Comment

# Create your views here.
class LibraryView(generic.TemplateView):
    template_name = "the_edda_library/the_edda_library.html"