from django.contrib import admin
from .models import Lore, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Lore)
class LoreAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author__username', 'is_deletion_pending', 'excerpt',)
    search_fields = ('title', 'primary_source', 'author__username',)
    list_filter = ('status', 'is_deletion_pending',)
    actions = ['approve_deletion', 'publish_lore_entry',]
    filter_horizontal = ('entities',)

    @admin.action(description='Confirm and delete selected lore entries')
    def approve_deletion (self, request, queryset):
        to_delete = queryset.filter(is_deletion_pending=True)
        count = to_delete.count()
        to_delete.delete()
        self.message_user(request, f"Successfully removed {count} entries from the library")

    @admin.action(description='Approve and publish selected lore entries')
    def publish_lore_entry (self, request, queryset):
        to_publish = queryset.filter(status=0)
        count = to_publish.count()
        to_publish.update(status=1)
        self.message_user(request, f"Successfully published {count} entries to the library")


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('author__username', 'lore__title', 'approved', 'body')
    list_filter = ('approved',)
    actions = ['approve_comment',]

    @admin.action(description='Confirm and approve comments to be published to site')
    def approve_comment (self, request, queryset):
        to_approve = queryset.filter(approved=False)
        count = to_approve.count()
        to_approve.update(approved=True)
        self.message_user(request, f"Successfully approved and published {count} comments to relevent lore entries")

# Register your models here.

