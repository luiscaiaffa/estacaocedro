# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=100,  blank=True, null=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=20,  blank=True, null=True, verbose_name='Telefone')
    descricao = models.CharField(max_length=255,  blank=True, null=True, verbose_name='Descrição')
    is_visualizada = models.BooleanField(default=False, verbose_name='Visualizada ?')
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    class Meta:
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome


class Doacao(models.Model):

    MODALIDADE_CHOICES = (
        ('1', 'Boleto bancário'),
        ('2', 'Pagamento em Espécie'),
        ('3', 'Depósito bancário'),
        ('4', 'Débito automático')
    )

    nome = models.CharField(max_length=100, verbose_name='Nome')
    rg = models.CharField(max_length=12, verbose_name='RG')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    telefone = models.CharField(max_length=20,  blank=True, null=True, verbose_name='Telefone Residencial')
    celular = models.CharField(max_length=21,  blank=True, null=True, verbose_name='Telefone Celular')
    cep = models.CharField(max_length=10, blank=True, null=True, verbose_name='CEP')
    rua = models.CharField(max_length=255, verbose_name='Rua')
    bairro = models.CharField(max_length=50,verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='UF')
    is_visualizada = models.BooleanField(default=False, verbose_name='Visualizada ?')
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    valor = models.CharField(max_length=255, verbose_name='Valor doado mensalmente')
    modalidade = models.CharField(max_length=20,  verbose_name='Modalidade de Pagamento', choices=MODALIDADE_CHOICES)

    # CAMPOS OPCIONAIS
    banco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Banco')
    conta  = models.CharField(max_length=20, blank=True, null=True, verbose_name='Conta')
    agencia  = models.CharField(max_length=10, blank=True, null=True, verbose_name='Agência')
    titular  = models.CharField(max_length=100, blank=True, null=True, verbose_name='Titular')
    cpf_cnpj  = models.CharField(max_length=30, blank=True, null=True, verbose_name='CPF/CNPJ')
    class Meta:
        verbose_name_plural = 'Doações'

    def __str__(self):
        return self.nome
