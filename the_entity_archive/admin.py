from django.contrib import admin
from .models import Entity
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entity)
class EntityAdmin(SummernoteModelAdmin):
    summernote_fields = ('biography',)
    list_display = ('name', 'status', 'author__username',
                    'lore_count', 'is_deletion_pending')
    search_fields = ('name', 'epithets', 'status', 'author__username',)
    list_filter = ('status', 'is_deletion_pending',)
    actions = ['approve_deletion', 'publish_entity', ]

    @admin.action(description='Confirm and delete selected entities')
    def approve_deletion(self, request, queryset):
        to_delete = queryset.filter(is_deletion_pending=True)
        count = to_delete.count()
        to_delete.delete()
        self.message_user(request,
                          f"Successfully removed {count} entities from the archive")

    @admin.action(description='Approve and publish selected entities')
    def publish_entity(self, request, queryset):
        to_publish = queryset.filter(status=0)
        count = to_publish.count()
        to_publish.update(status=1)
        self.message_user(request,
                          f"Successfully published {count} entities to the archive")

# Register your models here.
