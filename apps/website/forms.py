# -*- coding: utf-8 -*-
from django import forms
from .models import Contato, Doacao 

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'descricao']

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'

        self.fields['telefone'].widget.attrs['class'] = 'form-control'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'
        self.fields['telefone'].widget.attrs['data-validation'] = '[NOTEMPTY]'

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Mensagem'

        
class DoacaoForm(forms.ModelForm):

    class Meta:
        model = Doacao
        fields = ['nome', 'rg', 'cpf', 'email', 'telefone', 'celular', 'cep', 'rua', 
            'bairro', 'cidade', 'estado', 'valor', 'modalidade', 'banco', 'conta', 
            'agencia', 'titular', 'cpf_cnpj']

    def __init__(self, *args, **kwargs):
        super(DoacaoForm, self).__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

        self.fields['rg'].widget.attrs['class'] = 'form-control'
        self.fields['rg'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['rg'].widget.attrs['placeholder'] = 'RG'

        self.fields['cpf'].widget.attrs['class'] = 'form-control cpf'
        self.fields['cpf'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['cpf'].widget.attrs['placeholder'] = 'CPF'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['telefone'].widget.attrs['class'] = 'form-control telefone'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone Fixo'

        self.fields['celular'].widget.attrs['class'] = 'form-control celular'
        self.fields['celular'].widget.attrs['placeholder'] = 'Telefone Celular'

        self.fields['cep'].widget.attrs['class'] = 'form-control cep'
        self.fields['cep'].widget.attrs['placeholder'] = 'CEP'
        
        self.fields['rua'].widget.attrs['class'] = 'form-control'
        self.fields['rua'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['rua'].widget.attrs['placeholder'] = 'Endereço'

        self.fields['bairro'].widget.attrs['class'] = 'form-control'
        self.fields['bairro'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['bairro'].widget.attrs['placeholder'] = 'Bairro'

        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Cidade'
        
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['estado'].widget.attrs['placeholder'] = 'UF'

        self.fields['valor'].widget.attrs['class'] = 'form-control dinheiro'
        self.fields['valor'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['valor'].widget.attrs['placeholder'] = 'Valor (R$)'

        self.fields['modalidade'].widget.attrs['class'] = 'form-control'
        self.fields['modalidade'].widget.attrs['data-validation'] = '[NOTEMPTY]'

        # OPCIONAIS

        self.fields['banco'].widget.attrs['class'] = 'form-control'
        self.fields['banco'].widget.attrs['placeholder'] = 'Banco'
        
        self.fields['conta'].widget.attrs['class'] = 'form-control'
        self.fields['conta'].widget.attrs['placeholder'] = 'Conta'

        self.fields['agencia'].widget.attrs['class'] = 'form-control'
        self.fields['agencia'].widget.attrs['placeholder'] = 'Agência'
        
        self.fields['titular'].widget.attrs['class'] = 'form-control'
        self.fields['titular'].widget.attrs['placeholder'] = 'Titular'

        self.fields['cpf_cnpj'].widget.attrs['class'] = 'form-control'
        self.fields['cpf_cnpj'].widget.attrs['placeholder'] = 'CPF/CNPJ'       