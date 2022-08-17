from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Owner(models.Model):
    name = models.CharField(
        max_length=255, verbose_name=_("user")
    )

class Investments(models.Model):
    owner = models.ForeignKey(
        'Owner', on_delete=models.CASCADE, verbose_name=_("owner")
    )
    creation_date = models.DateField(
        verbose_name=_("created in"), validators=[MaxValueValidator(datetime.date.today)]
    )
    amount = models.DecimalField(
        max_digits=19, decimal_places=10, verbose_name=_("amount"), validators=[MinValueValidator(0)]
    )

    @property
    def owner_info(self):

        return {'testa': 'teste'}