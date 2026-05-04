from django.shortcuts import render
from django.views import generic
from .models import Lore

# Create your views here.
class LoreList(generic.ListView):
    queryset = Lore.objects.filter(status=1).order_by('-created_on')
    template_name = "the_edda_library/the_edda_library.html"
    paginate_by = 6