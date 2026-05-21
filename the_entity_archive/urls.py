from . import views
from django.urls import path


urlpatterns = [
    path("", views.EntityList.as_view(), name="archive"),
    path("<str:name>/", views.entity_profile, name="entity_profile"),
]
