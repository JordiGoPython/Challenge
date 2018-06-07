from django.db.models.signals import post_save, pre_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Product, Brand, Family, Type


def add_code_correlative(sender, instance, created, **kwargs):
    if created:
        instance.code = 400 + instance.pk
        instance.save()


def update_related_objects(sender, instance, *args, **kwargs):
    if instance.brand:
        instance.brand_name = instance.brand.name
    if instance.family:
        instance.family_name = instance.family.name
    if instance.type:
        instance.type_name = instance.type.type_name


def update_brand_name(sender, instance, created, **kwargs):
    for pr in instance.brand_products.all():
        pr.brand_name = instance.name
        pr.save()


def update_family_name(sender, instance, created, **kwargs):
    for pr in instance.family_products.all():
        pr.family_name = instance.name
        pr.save()


def update_type_name(sender, instance, created, **kwargs):
    for pr in instance.type_products.all():
        pr.type_name = instance.type_name
        pr.save()


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


pre_save.connect(update_related_objects, sender=Product,
                  dispatch_uid="update_related_objects")
post_save.connect(add_code_correlative, sender=Product,
                  dispatch_uid="add_code_correlative")
post_save.connect(update_brand_name, sender=Brand,
                  dispatch_uid="update_brand_name")
post_save.connect(update_family_name, sender=Family,
                  dispatch_uid="update_family_name")
post_save.connect(update_type_name, sender=Type,
                  dispatch_uid="update_type_name")
post_save.connect(create_auth_token, sender=User,
                  dispatch_uid="create_auth_token")