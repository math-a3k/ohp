from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User


class OHPUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class OHPUserAdmin(UserAdmin):

    form = OHPUserChangeForm
    list_display = (
        "user_type",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "date_joined",
        "is_staff",
    )
    list_display_links = ("username",)
    list_filter = ("user_type",) + UserAdmin.list_filter
    fieldsets = ((None, {"fields": ("user_type",)}),) + UserAdmin.fieldsets


admin.site.register(User, OHPUserAdmin)
