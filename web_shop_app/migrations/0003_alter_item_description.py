# Generated by Django 4.2.7 on 2023-11-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_shop_app', '0002_item_stripe_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
