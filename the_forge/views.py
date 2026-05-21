from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from the_edda_library.forms import LoreForm
from the_entity_archive.forms import EntityForm
from .forms import ContactDeveloperForm
from the_edda_library.models import Lore
from the_entity_archive.models import Entity


# Create your views here.
def forge_form(request):
    lore_form = LoreForm()
    entity_form = EntityForm()

    if request.method == "POST":

        # Check if the user is authenticated
        # before processing the form submission
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 "Only those who have declared their oath may enter the Forge. You must sign in or join our kin to share your wisdom and craft your contributions to the saga.")
            return redirect('login')

        # Determine which form was submitted
        # based on the name of the submit button
        if 'submit_lore' in request.POST:
            lore_form = LoreForm(data=request.POST or None,
                                 files=request.FILES)
            if lore_form.is_valid():
                lore = lore_form.save(commit=False)
                lore.author = request.user
                lore.save()
                lore_form.save_m2m()
                messages.add_message(request, messages.SUCCESS,
                                     "Your lore entry has been submitted and is awaiting approval.")
                return redirect('home')

        elif 'submit_entity' in request.POST:
            entity_form = EntityForm(data=request.POST or None,
                                     files=request.FILES)
            if entity_form.is_valid():
                entity = entity_form.save(commit=False)
                entity.author = request.user
                entity.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Your entity has been submitted and is awaiting approval.")
                return redirect('home')

    return render(request, 'the_forge/the_forge.html',
                  {'lore_form': lore_form,
                   'entity_form': entity_form})


def delete_lore(request, slug):
    """
    View to submit a lore for deletion by an admin
    """
    lore = get_object_or_404(Lore, slug=slug)

    if request.method == "POST":
        lore.is_deletion_pending = True
        lore.save()
        messages.add_message(request, messages.SUCCESS,
                             "Request for removal sent. The Valkyries will now decide its fate.")
        return redirect("lore_detail", slug=lore.slug)


def delete_entity(request, name):
    """
    View to submit an entity for deletion by an admin
    """
    entity = get_object_or_404(Entity, name=name)

    if request.method == "POST":
        entity.is_deletion_pending = True
        entity.save()
        messages.add_message(request, messages.SUCCESS,
                             "Request for removal sent. The Valkyries will now decide its fate.")
        return redirect("entity_profile", entity.name)


def contact_developer(request):
    if request.method == 'POST':
        contact_form = ContactDeveloperForm(data=request.POST)
        user_email = request.user.email
        user_message = request.POST.get('message')

        if contact_form.is_valid():
            email = EmailMessage(
                subject=f"New enquiry from {request.user.username}",
                body=user_message,
                from_email=None,
                to=['mimirsindex@gmail.com'],
                reply_to=[user_email]
            )

            email.send()

            messages.add_message(request, messages.SUCCESS,
                                 "Ratatoskr has taken flight! Your message is scuttling up the World Tree to the developer's ears—thank you for adding your voice to the branches of our community.")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Ratatoskr is a swift messenger, but it seems your message got tangled in the branches. Please check the form for errors and try again.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))
