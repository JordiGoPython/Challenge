# Generated by Django 2.0.6 on 2018-06-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.AddField(
            model_name='product',
            name='offer_day_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offer_day_to',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offer_price_offer',
            field=models.DateTimeField(null=True),
        ),
    ]
