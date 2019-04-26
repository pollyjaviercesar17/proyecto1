# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from aparte.select import Selects
from alumno.models import Account
from django.utils.translation import ugettext, ugettext_lazy as apodo
# Create your models here.


class Vivienda(models.Model):

	#vivienda
	tipo_vivienda = models.CharField(apodo('TIPO DE VIVIENDA'), max_length=20, null=True, blank=True, choices=Selects().tipo())
	
	#tenencia de la vivienda
	tenencia_vivienda = models.CharField(apodo('TENENCIA DE LA VIVIENDA'),max_length= 20, null=True, blank=True, choices=Selects().tenencias())

	#distribucion espacial
	num_dormitorio = models.IntegerField(apodo('NUMERO DE DORMITORIO'),default=0, null=True, blank=True)
	sala_di = models.BooleanField(apodo('SALA'),)
	cocina_di = models.BooleanField(apodo('COCINA'),)
	comedor_di  = models.BooleanField(apodo('COMEDOR'),)
	bano_di = models.BooleanField(apodo('BAÑO'),)
	lavadero_di = models.BooleanField(apodo('LAVADERO'),)
	patio_di = models.BooleanField(apodo('PATIO'),)
	garaje_di = models.BooleanField(apodo('GARAJE'),)
	jardin_di  = models.BooleanField(apodo('JARDIN'),)	

	#equipamiento de la vivienda
	nevera_eq = models.IntegerField(apodo('NEVERA(S)'),default=0, null=True, blank=True)
	cocina_eq = models.IntegerField(apodo('COCINA(S)'),default=0, null=True, blank=True)
	tv_eq = models.IntegerField(apodo('TELEVISOR(ES)'),default=0, null=True, blank=True)
	dvd_eq = models.IntegerField(apodo('DVD'),default=0, null=True, blank=True)
	ventiladores_eq = models.IntegerField(apodo('VENTILADOR(ES)'),default=0, null=True, blank=True)
	a_a_eq = models.IntegerField(apodo('AIRE ACONDICIONADO'),default=0, null=True, blank=True)
	computadora_eq = models.IntegerField(apodo('COMPUTADORA(S)'),default=0, null=True, blank=True)
	lavadora_eq = models.IntegerField(apodo('LAVADORA'),default=0, null=True, blank=True)
	recibo_eq = models.IntegerField(apodo('RECIBO'),default=0, null=True, blank=True)
	comedor_eq = models.IntegerField(apodo('COMEDOR(ES)'),default=0, null=True, blank=True)
	camas_eq = models.IntegerField(apodo('CAMA(S)'),default=0, null=True, blank=True)

	#servicios
	agua_se = models.BooleanField(apodo('AGUA'),)
	red_cloacas_se = models.BooleanField(apodo('RED DE CLOACAS'),)
	electricidad_se = models.BooleanField(apodo('ELECTRICIDAD'),)
	internet_se = models.BooleanField(apodo('INTERNET'),)
	tv_cable_se = models.BooleanField(apodo('TV POR CABLE'),)
	telefono_se = models.BooleanField(apodo('TELEFONO'),)
	trans_publico_se = models.BooleanField(apodo('TRANSPORTE PUBLICO'),)
	aseo_urba_se = models.BooleanField(apodo('ASEO URBANICO'),)

	alumno = models.ForeignKey(Account)

