# Generated by Django 3.2.4 on 2021-07-27 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210727_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='property',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='main_photo',
            field=models.ImageField(upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
    ]
