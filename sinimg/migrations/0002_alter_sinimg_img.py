# Generated by Django 3.2.15 on 2022-10-22 12:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sinimg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinimg',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]