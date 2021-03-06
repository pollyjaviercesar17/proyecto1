# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-18 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_familiar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosfamiliar',
            name='apell_f',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='ced_f',
            field=models.IntegerField(unique=True, verbose_name='C\xe9dula'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='fecha_naci',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='ingreso_mensual',
            field=models.IntegerField(verbose_name='Ingreso mensual'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='nivel_intr',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Nivel de intrucci\xf3n'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='nom_f',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='datosfamiliar',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Ocupaci\xf3n'),
        ),
    ]
