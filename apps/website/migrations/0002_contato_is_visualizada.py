# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='is_visualizada',
            field=models.BooleanField(default=False, verbose_name='Visualizada ?'),
        ),
    ]
