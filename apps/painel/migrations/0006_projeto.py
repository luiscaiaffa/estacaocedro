# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 13:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('painel', '0005_publicacao_resumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, unique=True, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Publicação')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
