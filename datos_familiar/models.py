# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from alumno.models import	Account
from aparte.select import Selects
from datetime import datetime
# Create your models here.

class DatosFamiliar(models.Model):
	ced_f = models.IntegerField('Cédula', unique=True)
	nom_f = models.CharField('Nombre', max_length=45, null=True, blank=True)
	apell_f = models.CharField('Apellido', max_length=45, null=True, blank=True)
	fecha_naci = models.DateField('Fecha de nacimiento', null=True)
	nivel_intr = models.CharField('Nivel de intrucción', max_length=45, null=True, blank = True)
	ocupacion = models.CharField('Ocupación', max_length = 45, null =True, blank = True)
	ingreso_mensual = models.IntegerField('Ingreso mensual')
	relationship = models.CharField('Parentesco', max_length=45, choices=Selects().parentesco())
	alumno = models.ForeignKey(Account)


	def __unicode__(self):
		Dato ="%i "%(self.ced_f)
		return Dato

	def get_full_name(self):
		return ' '.join([self.nom_f, self.apell_f])


	def edad(self):
		return int((datetime.now().date() - self.fecha_naci).days / 365.25)
