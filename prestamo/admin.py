# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from prestamo.models import Cliente, Formulario, Recurso

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Formulario)
admin.site.register(Recurso)