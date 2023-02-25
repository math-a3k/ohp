from django.db import models
from django.utils.translation import gettext as _


class Unit(models.Model):
    """
    UCUM Unit
    """

    code = models.CharField(
        _("Code"),
        max_length=10,
    )
    unit_class = models.CharField(
        _("Unit Class"),
        max_length=10,
    )
    is_metric = models.BooleanField(_("Is Metric?"), default=True)
    name = models.CharField(_("Name"), max_length=50)
    print_symbol = models.CharField(
        _("Print Symbol"), max_length=50, blank=True, null=True
    )
    unit_property = models.CharField(
        _("Unit Property"), max_length=50, blank=True, null=True
    )
    unit = models.CharField(_("Unit"), max_length=10, blank=True, null=True)
    unit_value = models.CharField(
        _("Value"), max_length=10, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):  # pragma: no cover
        return f"{self.code} ({self.name}) [{self.print_symbol}]"
