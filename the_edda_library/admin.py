from django.contrib import admin
from .models import Lore, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Lore)
class LoreAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'author__username',)
    search_fields = ('title', 'primary_source', 'author__username',)
    list_filter = ('status',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('author__username', 'lore__title', 'approved',)
    list_filter = ('approved',)

# Register your models here.

