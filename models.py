from django.db import models
from django.utils.translation import gettext_lazy as _

class Device(models.Model):
    class UsageMode(models.TextChoices):
        STUDENT = 'SU', _('Student')
        GENERAL = 'GU', _('General User')
      
    device = models.CharField(max_length=20,primary_key=True,unique=True)
    location = models.CharField(max_length=15,unique=True)
    mode = models.CharField(
        max_length=2,
        choices=UsageMode.choices,
        default=UsageMode.STUDENT,
    )

