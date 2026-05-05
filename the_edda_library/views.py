from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Lore, Comment

# Create your views here.
class LoreList(generic.ListView):
    model = Lore
    template_name = "the_edda_library/the_edda_library.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Override the default queryset to allow sorting based on query parameters.

        **Context:**

        `sort_by`
            A string obtained from the query parameters that determines the sorting order.

        **Template**

        :template:`the_edda_library/the_edda_library.html`
        
        """
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
        """
        Override the default context data to include the current sort parameter.

        **Context:**

        `current_sort`
            A string indicating the current sorting order.

        **Template**

        :template:`the_edda_library/the_edda_library.html`

        """
        context = super().get_context_data(**kwargs)
        context["current_sort"] = self.request.GET.get("sort", "newest")
        return context
    
def lore_detail(request, slug):
    """
    View function to display the details of a specific lore entry.

    **Context:**

    `lore`
        An instance of the Lore model corresponding to the provided slug.

    **Template**

    :template:`the_edda_library/lore_detail.html`

    """
    queryset = Lore.objects.filter(status=1)
    lore = get_object_or_404(queryset, slug=slug)

    return render(request, "the_edda_library/lore_detail.html", {"lore": lore})