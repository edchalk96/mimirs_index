from django.views import generic
from .models import Lore

# Create your views here.
class LoreList(generic.ListView):
    model = Lore
    template_name = "the_edda_library/the_edda_library.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get("sort", "newest")

        if sort_by == "az":
            return queryset.order_by("title")
        elif sort_by == "za":
            return queryset.order_by("-title")
        elif sort_by == "oldest":
            return queryset.order_by("created_on")
        else:  # Default to newest
            return queryset.order_by("-created_on")
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_sort"] = self.request.GET.get("sort", "newest")
        return context