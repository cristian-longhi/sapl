# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0018_auto_20160510_0943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='legislatura',
            options={'ordering': ['-data_inicio'], 'verbose_name': 'Legislatura', 'verbose_name_plural': 'Legislaturas'},
        ),
    ]
