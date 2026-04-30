from . import views
from django.urls import path

urlpatterns = [
    path("", views.ForgeView.as_view(), name="forge"),
]