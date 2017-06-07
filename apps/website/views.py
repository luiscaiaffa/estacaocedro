# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

from .forms import ContatoForm, DoacaoForm
from apps.painel.models import Publicacao, Projeto, Album, Imagem


class Home(View):
    def get(self, request):
    	publicacoes = Publicacao.objects.all().order_by('-data')[:3]
    	projetos = Projeto.objects.all().order_by('-data')[:6]
    	albuns = Album.objects.all().order_by('-data')[:4]
    	imagens = Imagem.objects.all().order_by('-album__data')

    	galeria = []
    	for album in albuns:
    		for imagem in imagens:
    			if album.pk == imagem.album.pk:
    				galeria.append(imagem)
    				break
    			pass
    		pass
    	pass

    	context = {'publicacoes':publicacoes, 'projetos':projetos, 'galeria':galeria}
    	return render (request, 'index.html', context)



class Sobre(View):
    def get(self, request):
    	context = {}
    	return render (request, 'sobre.html', context) 


class Galeria(View):
	def get(self, request, pk):
		imagens = Imagem.objects.filter(album=pk)
		context = {'imagens':imagens}
		return render(request, 'galeria/galeria.html', context)


class ListaGaleria(View):
	def get(self, request):
		albuns = Album.objects.all().order_by('-data')[:4]
		imagens = Imagem.objects.all().order_by('-album__data')

		galeria = []
		for album in albuns:
			for imagem in imagens:
				if album.pk == imagem.album.pk:
					galeria.append(imagem)
					break
				pass
			pass
			
		context = {'galeria':galeria}
		return render(request, 'galeria/list.html', context)


class Noticia(View):
	def get(self, request, pk):
		publicacao = Publicacao.objects.get(pk=pk)
		context = {'publicacao':publicacao}
		return render(request, 'noticia/noticia.html', context)

class ListaNoticias(View):
	def get(self, request):
		publicacoes = Publicacao.objects.all()
		context = {'publicacoes':publicacoes}
		return render(request, 'noticia/list.html', context)



class Contato(View):
	def get(self, request):
		form = ContatoForm
		context = {'form':form, 'message':False}
		return render (request, 'contato.html', context)

	def post(self, request, *args, **kwargs):
		form = ContatoForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
		form = ContatoForm()
		context = {'form':form, 'message':True}
		return render (request, 'contato.html', context)



class Doacao(View):
	def get(self, request):
		form = DoacaoForm
		context = {'form':form, 'message':False}
		return render (request, 'doacao.html', context)

	def post(self, request, *args, **kwargs):
		form = DoacaoForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form = DoacaoForm()
			context = {'form':form, 'message':True}
		else:
			context = {'form':form, 'message':False}
			
		return render (request, 'doacao.html', context)