from . import views
from django.urls import path

urlpatterns = [
    path("", views.LoreList.as_view(), name="library"),
    path("<slug:slug>/", views.lore_detail, name="lore_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
