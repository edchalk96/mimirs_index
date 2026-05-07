from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from the_edda_library.forms import LoreForm
from the_entity_archive.forms import EntityForm
from .forms import ContactDeveloperForm


# Create your views here.
@login_required
def forge_form(request):
    lore_form = LoreForm()
    entity_form = EntityForm()

    if request.method == 'POST':
        if 'submit_lore' in request.POST:
            if lore_form.is_valid():
                lore_form = LoreForm(data=request.POST or None, prefix='lore')
                lore = lore_form.save(commit=False)
                lore.author = request.user
                lore.save()
                messages.add_message(request, messages.SUCCESS, "Your lore entry has been submitted and is awaiting approval.")
                return redirect('lore_detail', slug=lore.slug)
            
        elif 'submit_entity' in request.POST:
            if entity_form.is_valid():
                entity_form = EntityForm(data=request.POST or None, prefix='entity')
                entity = entity_form.save(commit=False)
                entity.author = request.user
                entity.save()
                messages.add_message(request, messages.SUCCESS, "Your entity entry has been submitted and is awaiting approval.")
                return redirect('entity_profile', str=entity.name)
            
    return render(request, 'the_forge/the_forge.html', {'lore_form': lore_form, 'entity_form': entity_form})


def contact_developer(request):
    if request.method == 'POST':
        contact_form = ContactDeveloperForm(data=request.POST)
        if contact_form.is_valid():
            send_mail(
                subject=contact_form.cleaned_data['subject'],
                message=contact_form.cleaned_data['message'],
                from_email=contact_form.cleaned_data['email'],
                recipient_list=['edchalk96@gmail.com'],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, "Ratatoskr has taken flight! Your message is scuttling up the World Tree to the developer's ears—thank you for adding your voice to the branches of our community.")
        else:
            messages.add_message(request, messages.ERROR, "Ratatoskr is a swift messenger, but it seems your message got tangled in the branches. Please check the form for errors and try again.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))
        