# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contato, Doacao

admin.site.register(Contato)
admin.site.register(Doacao)