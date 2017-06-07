# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_contato_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('rg', models.CharField(max_length=12, verbose_name='RG')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone Residencial')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone Celular')),
                ('cep', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('rua', models.CharField(blank=True, max_length=255, null=True, verbose_name='Rua')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
            ],
            options={
                'verbose_name_plural': 'Doações',
            },
        ),
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]