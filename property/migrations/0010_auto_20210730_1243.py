# Generated by Django 3.2.4 on 2021-07-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_property_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='MainPhoto',
            field=models.ImageField(upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Bathrooms'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Bedrooms'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage',
            field=models.IntegerField(default=0, verbose_name='Garage'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=255, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(help_text='Title of the property', max_length=255, verbose_name='Title'),
        ),
    ]