from django.db import models
from .constants import TYPE
from .core.models import BaseTimeModel


# Create your models here.
class Brand(BaseTimeModel):
    name = models.CharField(max_length=120, blank=True)
    brand_field = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Family(BaseTimeModel):
    name = models.CharField(max_length=120, blank=True)
    family_field = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Type(BaseTimeModel):
    type_name = models.CharField(max_length=2, choices=TYPE)
    type_field = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{0}'.format(self.type_name)


class Product(BaseTimeModel):
    code = models.IntegerField(editable=False, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True)
    description = models.CharField(max_length=120, blank=True)
    is_variation = models.BooleanField(default=False)
    is_complement = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    brand_name = models.CharField(max_length=120, blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE, blank=True, null=True)
    family_name = models.CharField(max_length=120, blank=True, null=True)
    family = models.ForeignKey(Family, related_name='family_products', on_delete=models.CASCADE, blank=True, null=True)
    type_name = models.CharField(max_length=2, blank=True, null=True)
    type = models.ForeignKey(Type, related_name='type_products', on_delete=models.CASCADE, blank=True, null=True)
    offer_day_from = models.DateTimeField(null=True)
    offer_day_to = models.DateTimeField(null=True)
    offer_price_offer = models.DateTimeField(null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.code)


class ProductDetail(BaseTimeModel):
    product = models.OneToOneField(Product, related_name='detail_product', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=1)
    quantity = models.IntegerField(default=1)
    sku = models.CharField(max_length=20, blank=True, null=True)
