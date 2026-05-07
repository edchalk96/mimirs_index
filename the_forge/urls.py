from . import views
from django.urls import path

urlpatterns = [
    path('', views.forge_form, name='forge'),
    path('delete-lore/<slug:slug>/', views.delete_lore, name='delete_lore'),
    path('contact-developer/', views.contact_developer, name='contact_developer'),
]