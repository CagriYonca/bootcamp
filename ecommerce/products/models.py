from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from products import enums


class Product(BaseAbstractModel):
    sku = models.CharField(verbose_name=_("SKU"), max_length=100, unique=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    color = models.CharField(
        choices=enums.Colors.choices, verbose_name=_("Color"), max_length=20)
    size = models.CharField(max_length=30, verbose_name=_("Size"))

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.sku
