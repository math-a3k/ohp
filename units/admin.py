from django.contrib import admin

from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "print_symbol", "unit_class")
    list_filter = ("unit_class",)
    search_fields = ("code", "name", "print_symbol")


admin.site.register(Unit, UnitAdmin)
