from django.contrib import admin
from .models import Entity
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Entity)
class EntityAdmin(SummernoteModelAdmin):
    summernote_fields = ('biography',)
    list_display = ('entity_name', 'status', 'author__username', 'lore_count',)
    search_fields = ('entity_name', 'epithets', 'status', 'author__username',)
    list_filter = ('status',)

# Register your models here.
