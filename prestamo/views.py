# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from prestamo.models import Cliente, Formulario, Recurso
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets


#CLIENTE
'''
def cliente(request):
		cliente_list=Cliente.objects.all()
		context = {'object_list':cliente_list}
		return render(request, 'prestamo/cliente.html', context)

def cliente_detail(request, cliente_id):
		cliente=Cliente.objects.get(id=cliente_id)
		context = {'object':category}
		return render(request, 'prestamo/cliente_detail.html', context)'''
@login_required
def base(request):
	return render(request, 'base.html')

class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls):
		return login_required(super(LoginRequiredMixin, cls).as_view())



class ClienteList(LoginRequiredMixin, ListView):
	login_required = True
	model=Cliente


class ClienteDetail(LoginRequiredMixin, DetailView):
	login_required = True
	model=Cliente		

class ClienteUpdate(LoginRequiredMixin, UpdateView):
	login_required = True
	model=Cliente
	fields='__all__'

class ClienteDelete(LoginRequiredMixin, DeleteView):
	login_required = True
	model=Cliente
	success_url=reverse_lazy('cliente-list')

class ClienteCreate(LoginRequiredMixin, CreateView):
	login_required = True
	model=Cliente
	fields='__all__'

#FORMULARIO

class FormularioListView(LoginRequiredMixin, ListView):
	login_required = True
	model=Formulario		

class FormularioDetailView(LoginRequiredMixin, DetailView):
	login_required = True
	model=Formulario	

class FormularioCreate(LoginRequiredMixin, CreateView):
	login_required = True
	model=Formulario
	fields='__all__'

class FormularioUpdate(LoginRequiredMixin, UpdateView):
	login_required = True
	model=Formulario
	fields='__all__'

class FormularioDelete(LoginRequiredMixin, DeleteView):
	login_required = True
	model=Formulario
	success_url=reverse_lazy('formulario-list')

#Recursos

class RecursoListView(LoginRequiredMixin, ListView):
	login_required = True
	model=Recurso	

class RecursoDetailView(LoginRequiredMixin, DetailView):
	login_required = True
	model=Recurso

class RecursoCreate(LoginRequiredMixin, CreateView):
	login_required = True
	model=Recurso
	fields='__all__'

class RecursoUpdate(LoginRequiredMixin, UpdateView):
	login_required = True
	model=Recurso
	fields='__all__'

class RecursoDelete(LoginRequiredMixin, DeleteView):
	login_required = True
	model=Recurso
	success_url=reverse_lazy('formulario-list')

@login_required
def Prestamos (request,recurso_id):
    objeto=Recurso.object.get(recurso_id)
    objeto.cantidad=objeto.cantidad-1
	#objeto.save()


	