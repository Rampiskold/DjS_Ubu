# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170617_1806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '\u0422\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': '\u0424\u043e\u0442\u043e', 'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438'},
        ),
    ]
