from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Entity
from .forms import EntityForm
from django.contrib import messages

# Create your views here.
class EntityList(generic.ListView):
    queryset = Entity.objects.filter(status=1)
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
    
def entity_profile(request, name):
    """
    View function to display the profile of a specific entity as well suggest edits.

    **Context:**

    `entity`
        An instance of the Entity model that matches the provided name.

    **Template**

    :template:`the_entity_archive/entity_profile.html`

    """
    queryset = Entity.objects.filter(status=1)
    entity = get_object_or_404(queryset, name=name)

    edit_entity_form = EntityForm(instance=entity)

    if request.method == "POST":
        edit_entity_form = EntityForm(data=request.POST, instance=entity, files=request.FILES)

        if edit_entity_form.is_valid():
            entity = edit_entity_form.save(commit=False)
            entity.status = 0
            entity.save()
            messages.add_message(request, messages.SUCCESS, "The entity has been re-forged. Awaiting Mimir's approval")
            return redirect("archive")


    return render(request, "the_entity_archive/entity_profile.html", {"entity": entity, "edit_entity_form": edit_entity_form})