# Generated by Django 3.2.20 on 2023-08-13 08:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_auto_20230812_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=cloudinary.models.CloudinaryField(default='media/user-default.webp', max_length=255, verbose_name='profile_image'),
        ),
    ]
