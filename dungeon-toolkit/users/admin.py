from django.contrib import admin
from users.models import User
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)


class CustomUserAdmin(UserAdmin):
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.photo.url)
        return "No Photo"

    photo_preview.short_description = "Profile Photo"

    list_display = ('username', 'email', 'photo_preview',
                    'is_staff', 'is_active')
    readonly_fields = ('photo_preview',)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("photo", "photo_preview")}),
    )
