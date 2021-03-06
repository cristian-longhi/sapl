# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-04 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coligacao',
            name='numero_votos',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nº Votos Recebidos (Coligação)'),
        ),
        migrations.AlterField(
            model_name='mandato',
            name='votos_recebidos',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Votos Recebidos (Mandato)'),
        ),
    ]
