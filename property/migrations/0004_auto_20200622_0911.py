# Generated by Django 3.0.7 on 2020-06-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
