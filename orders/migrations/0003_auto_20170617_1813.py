# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_customer_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u0417\u0430\u043a\u0430\u0437', 'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': '\u0422\u043e\u0432\u0430\u0440 \u0432 \u0437\u0430\u043a\u0430\u0437\u0435', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b \u0432 \u0437\u0430\u043a\u0430\u0437\u0435'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u0437\u0430\u043a\u0430\u0437\u0430'},
        ),
    ]
