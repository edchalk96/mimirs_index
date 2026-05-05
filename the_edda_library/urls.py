from . import views
from django.urls import path

urlpatterns = [
    path("", views.LoreList.as_view(), name="library"),
    path("<slug:slug>/", views.lore_detail, name="lore_detail"),
]