from django.contrib import admin
from .models import ChatGroup
# Register your models here.
class ChatGroupAdmin(admin.ModelAdmin):
    """ enable group chat admin"""

    list_display = ("id","name","description", "icon", "mute_notifications","icon", )
    list_filter = ("id","name","description", "icon", "mute_notifications","icon", )
    list_display_links = ("name", )

admin.site.register(ChatGroup,ChatGroupAdmin)