# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse
# Create your models here.
class Cliente(models.Model):
	"""docstring for Cliente"""
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	def get_absolute_url(self):
		return reverse ('cliente-list')
	def __str__(self):
		return self.nombre

class Recurso(models.Model):
	"""docstring for Recursos"""
	nombre_recurso = models.CharField(max_length=50)
	cantidad = models.IntegerField()
	def get_absolute_url(self):
		return reverse ('recursos-list')
	def __str__(self):
		return self.nombre_recurso

class Formulario(models.Model):
	"""docstring for Formulario"""
	nombreCliente = models.ForeignKey(Cliente)
	nombreRecurso = models.ForeignKey(Recurso)
	conceptoPrestamo = models.CharField(max_length=1000)
	fechaPrestamo = models.DateTimeField(auto_now_add= True)
	fechaDevolucion = models.DateTimeField()
	def get_absolute_url(self):
		return reverse ('formulario-list')
	def __str__(self):
		return self.conceptoPrestamo