from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User Model for ohp
    """

    PATIENT = 0
    HOSPITAL = 1

    USER_TYPE_CHOICES = (
        (PATIENT, _("Patient")),
        (HOSPITAL, _("Hospital")),
    )

    user_type = models.PositiveSmallIntegerField(
        _("User Type"), choices=USER_TYPE_CHOICES, default=HOSPITAL
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
