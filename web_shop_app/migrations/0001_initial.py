# Generated by Django 4.2.7 on 2023-11-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('price', models.FloatField(default=1.0)),
            ],
        ),
    ]
