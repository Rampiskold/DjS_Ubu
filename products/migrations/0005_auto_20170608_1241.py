# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170608_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=b'products_images/'),
        ),
    ]
