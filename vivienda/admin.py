# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from vivienda.models import *

# Register your models here.
class AdminVivienda(admin.ModelAdmin):
	list_display = ['__unicode__', 'tipo_vivienda', 'tenencia_vivienda']

	class Meta:
		model = Vivienda
admin.site.register(Vivienda, AdminVivienda)

