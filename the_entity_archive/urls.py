from . import views
from django.urls import path

urlpatterns = [
    path("", views.ArchiveView.as_view(), name="archive"),
]