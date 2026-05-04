from django.shortcuts import render
from django.views import generic
from .models import Lore
import random

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "home/index.html"

# Function to pull through a random Lore entry for the homepage - Credit to https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html for this information on how to do this.
def random_lore(request):
    count = Lore.objects.count()
    random_lore = None

    if count > 0:
        random_index = random.randint(0, count - 1)
        random_lore = Lore.objects.prefetch_related('entities').all()[random_index]

    return render(request, 'home/index.html', {'random_lore': random_lore})