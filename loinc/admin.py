from django.contrib import admin

from .models import Loinc


class LoincAdmin(admin.ModelAdmin):
    list_display = (
        "loinc_num",
        "display_name",
    )
    list_filter = ("component",)
    search_fields = ("code", "name", "print_symbol")


admin.site.register(Loinc, LoincAdmin)
