# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db import connection as conector
from alumno.models import Account, Alumno_beca
import time

class Sql():
    resultado = None
    def __init__(self, query, numero):
        x = conector.cursor()
        x.execute(query)
        columns = [col[0] for col in x.description]
        print columns
        if numero == 1:
            data = x.fetchall() or columns			
            self.resultado= [dict(zip(columns, row)) for row in data]
        elif numero == 2:
            data = x.fetchone() or columns
            self.resultado = dict(zip(columns, data))
        print data

class ListarAlumno(LoginRequiredMixin, FormView):
	template_name = 'reporte/listadoalumno.html'

	def get(self, request, *args, **kwargs):
		query = "SELECT * FROM  alumno_alumno_beca AS aa LEFT JOIN alumno_account AS a ON aa.alumno_id = a.id LEFT JOIN acta_acta AS ac ON aa.id = ac.alumno_id ORDER BY aa.updated_at"
		cursor = Sql(query, 1)
		print cursor.resultado
		return render(request, self.template_name, {
												'form':cursor.resultado
												})

class ListarAlumnoFalse(LoginRequiredMixin, FormView):
	template_name = 'reporte/listadoalumno.html'

	def get(self, request, *args, **kwargs):
		query = "SELECT * FROM  alumno_alumno_beca AS aa LEFT JOIN alumno_account AS a ON aa.alumno_id = a.id LEFT JOIN acta_acta AS ac ON aa.id = ac.alumno_id WHERE (ac.status IS NULL OR ac.status=0) ORDER BY aa.updated_at"
		cursor = Sql(query, 1)
		print cursor.resultado
		return render(request, self.template_name, {
												'form':cursor.resultado
												})

class ListarAlumnoTrue(LoginRequiredMixin, FormView):
	template_name = 'reporte/listadoalumno.html'

	def get(self, request, *args, **kwargs):
		query = "SELECT * FROM  alumno_alumno_beca AS aa LEFT JOIN alumno_account AS a ON aa.alumno_id = a.id LEFT JOIN acta_acta AS ac ON aa.id = ac.alumno_id WHERE ac.status=1 ORDER BY aa.updated_at"
		cursor = Sql(query, 1)
		print cursor.resultado
		return render(request, self.template_name, {
												'form':cursor.resultado
												})

class PlanillaBeca(LoginRequiredMixin, FormView):
	template_name = 'reporte/planilla.html'

	def get(self, request, *args, **kwargs):
	    alu = get_object_or_404(Account, pk=self.kwargs['pk'])
	    alb= Alumno_beca.objects.filter(alumno=self.kwargs['pk']).first()
	    query = "SELECT aa.status, ac.ced_alu FROM alumno_alumno_beca AS ab LEFT JOIN alumno_account AS ac ON ab.alumno_id=ac.id LEFT JOIN acta_acta AS aa ON aa.alumno_id=ab.id WHERE ac.ced_alu = %s" % (alu.ced_alu)
	    cursor = Sql(query, 2)
	    ver =  cursor.resultado
	    titulo = ""
	    if ver['status'] is None:
	    	titulo = "SOLICITUD DE BECA"
	    elif ver['status'] == 0:
	    	titulo = "RENOVACION DE BECA"
	    elif ver['status'] == 1:
	    	titulo = "USTED YA TIENE LA BECA APROBADA"	    
	    me = {'01':'ENERO', '02':'FEBRERO', '03':'MARZO', '04':'ABRIL', '05':'MAYO', '06':'JUNIO',
	    	  		'07':'JULIO', '08':'AGOSTO', '09':'SEPTIEMBRE', '10':'OCTUBRE', 
	    	  								'11':'NOVIEMBRE', '12':'DICIEMBRE'}
	    mes= me[time.strftime("%m")]
	    return render(request, self.template_name, {'alumno':alu,
	    											'dia':time.strftime("%d"),
	    											'mes':mes,
	    											'ano':time.strftime("%Y"),
	    											'titulo':titulo,
	    											'alumnoo':alb,}
	    											)