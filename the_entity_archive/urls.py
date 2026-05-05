from . import views
from django.urls import path

urlpatterns = [
    path("", views.EntityList.as_view(), name="archive"),
    path("<name:name/", views.entity_Detail, name="entity_detail"),
]