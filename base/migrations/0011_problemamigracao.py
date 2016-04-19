# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0010_auto_20160309_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemaMigracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID do Objeto')),
                ('problema', models.CharField(max_length=300, null=True, verbose_name='Problema')),
                ('descricao', models.CharField(max_length=300, null=True, verbose_name='Descrição')),
                ('endereco', models.URLField(null=True, verbose_name='Endereço')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Tipo de Content')),
            ],
            options={
                'verbose_name_plural': 'Problemas na Migração',
                'verbose_name': 'Problema na Migração',
            },
        ),
    ]
