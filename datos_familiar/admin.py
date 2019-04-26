# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from datos_familiar import models


# Register your models here.

@admin.register(models.DatosFamiliar)
class DatosFamiliarModelAdmin(admin.ModelAdmin):
    list_display = ('ced_f', 'nom_f', 'apell_f', 'fecha_naci',)
    list_filter = ('nivel_intr' , 'ocupacion', 'ingreso_mensual',)
    search_fields = ['ci', 'first_name', 'last_name',]

                                     