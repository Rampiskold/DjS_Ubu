# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=b'static/media/products_images/'),
        ),
    ]