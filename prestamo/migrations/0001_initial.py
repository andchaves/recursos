# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conceptoPrestamo', models.CharField(max_length=1000)),
                ('fechaPrestamo', models.DateTimeField()),
                ('fechaDevolucion', models.DateTimeField()),
                ('nombreCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamo.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recurso', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
           
            ],
        ),
        migrations.AddField(
            model_name='formulario',
            name='nombreRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamo.Recurso'),
        ),
    ]