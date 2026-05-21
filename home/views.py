from django.views import generic
from the_edda_library.models import Lore
import random

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = "home/index.html"

# Function to pull through a random Lore entry for the homepage
# Credit to:
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
# for this information on how to do this.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approved_lore = Lore.objects.filter(status=1).prefetch_related('entities')
        count = approved_lore.count()
        random_lore = None
        if count > 0:
            random_index = random.randint(0, count - 1)
            random_lore = approved_lore[random_index]

        context['random_lore'] = random_lore

        return context
