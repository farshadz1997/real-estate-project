# Generated by Django 3.2.4 on 2021-07-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20210727_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='main_photo',
            new_name='MainPhoto',
        ),
    ]