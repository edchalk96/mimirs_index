from django.views import generic
from .models import Entity

# Create your views here.
class EntityList(generic.ListView):
    model = Entity
    template_name = "the_entity_archive/the_entity_archive.html"
    paginate_by = 8

    # Code for the search functionality in the entity archive
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_term"] = self.request.GET.get("q", "")
        return context
