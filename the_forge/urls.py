from . import views
from django.urls import path

urlpatterns = [
    path('', views.forge_form, name='forge'),
    path('contact-developer/', views.contact_developer, name='contact_developer'),
]