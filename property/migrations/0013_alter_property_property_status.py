# Generated by Django 3.2.4 on 2021-08-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_property_property_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_status',
            field=models.CharField(choices=[('FS', 'For Sale'), ('FR', 'For Rent'), ('SL', 'Sold Out')], max_length=2, verbose_name='Property status'),
        ),
    ]
