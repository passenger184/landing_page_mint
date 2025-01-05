from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin

from .models import FAQ, AboutUs, Announcement, Resource, HeroSection, Figure, GDOPComponent, SupportRequest


class BaseAdmin(ModelAdmin):
    exclude = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.unregister(User)
admin.site.unregister(Group)


def toggle_active_status(modeladmin, request, queryset):
    for user in queryset:
        user.is_active = not user.is_active
        user.save()
    modeladmin.message_user(
        request, "Selected users' active status has been toggled.")


toggle_active_status.short_description = "Toggle active status of selected users"


@admin.register(User)
class UserAdmin(BaseUserAdmin, BaseAdmin):
    actions = [toggle_active_status]
    list_display = ["username", "first_name",
                    "last_name", "email", "date_joined", "is_active"]


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, BaseAdmin):
    pass


@admin.register(HeroSection)
class HeroSectionAdmin(BaseAdmin):
    list_display = ["title", "subtitle",
                    "button_text", "created_at", "updated_at", 'created_by', 'updated_by']
    search_fields = ["title", "subtitle",
                     "button_text", 'created_by', 'updated_by']
    list_filter = ["created_at", "updated_at"]


@admin.register(GDOPComponent)
class GDOPComponentsAdmin(BaseAdmin):
    list_display = ['title', 'button_url', 'updated_at',
                    'is_active', 'updated_at', 'created_by', 'updated_by']
    list_filter = ('updated_at',)
    search_fields = ('title', 'description', 'button_text')


@admin.register(Announcement)
class AnnouncementAdmin(BaseAdmin):
    list_display = ['title', 'sub_title', 'updated_at',
                    'created_by', 'updated_by']
    search_fields = ('title', 'sub_title', 'description')


@admin.register(AboutUs)
class AboutUsAdmin(BaseAdmin):
    list_display = ['title', 'updated_at', 'created_by', 'updated_by']
    search_fields = ['title', 'description_1',
                     'description_2', 'bullet_points']
    list_filter = ['updated_at']


@admin.register(Figure)
class FiguresAdmin(BaseAdmin):
    list_display = ['title', 'value', 'updated_at', 'created_by', 'updated_by']
    search_fields = ['title', 'value']
    list_filter = ['title', 'value', 'updated_at']


@admin.register(FAQ)
class FAQAdmin(BaseAdmin):
    list_display = ['question', 'answer', 'order', 'created_by', 'updated_by']
    search_fields = ['question', 'answer']


@admin.register(Resource)
class ResourceAdmin(BaseAdmin):
    list_display = ['title', 'address', 'email', 'phone',
                    'updated_at', 'created_by', 'updated_by']


@admin.register(SupportRequest)
class SupportRequestAdmin(BaseAdmin):
    list_display = ['name', 'email', 'support_type', 'urgency', 'status']
    search_fields = ['name', 'email', 'support_type', 'description']
    list_filter = ['support_type', 'status', 'urgency']
    ordering = ['status']

    # Make all fields readonly except 'status' for admins
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in obj._meta.fields if field.name != 'status']
        return ['name', 'email', 'support_type', 'description', 'attachment', 'urgency', 'submitted_at', 'created_at', 'updated_at', 'status']
