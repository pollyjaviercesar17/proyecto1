#! -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
# django paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# class based views.
from django.views.generic import ListView, TemplateView, FormView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# models Aluyno
from alumno.models import *
from alumno.forms import *
from alumno.mixins import *

from django.db.models import Q

from django.contrib import messages

#models de Datos familiar
from datos_familiar import models
from datos_familiar.forms import DatosFamiliarModelForm
from django.db import connection as conector
#models de vivienda
from vivienda.models import Vivienda
from vivienda.forms import *


#models fame
from fame.models import Fame
from fame.forms import  FameModelForm

from acta.models import Acta
# Create your views here.
from login.views import LoginRequiredMixin

from alumno.date import add_month
from datetime import datetime, date

class Sql():
    resultado = None
    def __init__(self, query, numero):
        x = conector.cursor()
        x.execute(query)
        columns = [col[0] for col in x.description]
        if numero == 1:
            self.resultado= [dict(zip(columns, row)) for row in x.fetchall()]
        elif numero == 2:
            self.resultado = dict(zip(columns, x.fetchone()))

class AlumnoListView(LoginRequiredMixin, ListView):
    model = Alumno_beca
    paginate_by = 30
    template_name = 'alumno/account_list.html'

    def get_context_data(self, **kwargs):
        context = super(AlumnoListView, self).get_context_data(**kwargs)
        hoy = date.today()
        mes = hoy.month
        year = hoy.year
        dia = hoy.day
        d = datetime(year, mes, dia)
        aj = add_month(d, -6)
        ajaa = self.model.objects.filter(updated_at__range=("1990-01-01 1:0:0", str(aj)))
        print ajaa
        for i in ajaa:
            print i.alumno
            acta = Acta.objects.filter(alumno=i.alumno, status=True)
            for j in acta:
                j.status = False
                j.save()
        ga = self.model.objects.all().order_by('-id')
        lista = []
        

        for i in ga:
            lista.append(i.id)
        if len(lista)!=0:
            context['aja'] = max(lista)
        else:
            context['aja'] = 0

        query = self.request.GET.get('alumno')
        query_result = None
        if query:
            ver = Account.objects.filter(ced_alu = query).first()
            if ver:
                aluu = Alumno_beca.objects.filter(alumno=ver.pk).first()
                if aluu:
                    query_result= Acta.objects.filter(alumno=aluu.pk)
            if not query_result:
                context["mensaje"] = "La Cedula %s No Existe" % (query)
                query_result = Acta.objects.filter(status=False)
        else:
            query_result = Acta.objects.filter(status=True)


        # paginator
        paginator = Paginator(query_result, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        context['object_list'] = object_list
        return context


class AlumnoallView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        aj =  request.GET["id"]
        ga = Alumno_beca.objects.raw('SELECT * FROM alumno_alumno_beca where id >  "' + str(aj) + '" ')
        #ga = Alumno_beca.objects.filter(id__gt=aj)
        return HttpResponse(ga)

class AlumnoTrueListView(LoginRequiredMixin, TemplateView):
    def get(self,request,*args, **kwargs):
        data = {}
        acu = 0
        vui = Acta.objects.filter(status=True)
        for i in vui:
            o = Alumno_beca.objects.get(pk=i.alumno_id)
            s = Account.objects.get(pk=o.alumno_id)
            data[acu] = {
            'id': str(s.id),
            'nombre': str(s.nom_alu) + " " + str(s.apell_alu),
            'cedula': str(s.tip_ced_alu) + " - "  + str(s.ced_alu),
            'foto': str(o.img) }
            acu+=1
        return JsonResponse(data)

class AlumnoFalseListView(LoginRequiredMixin, TemplateView):
    def get(self,request,*args, **kwargs):
        data = {}
        acu = 0
        q1 = Acta.objects.filter(status=True)
        q2 = Alumno_beca.objects.exclude(Q(pk__in=q1))
        #vui = Acta.objects.filter(status=True)
        for i in q2:
            s = Account.objects.get(pk = i.alumno_id)
            data[acu] = {
            'id': str(s.pk),
            'nombre': str(s.nom_alu) + " " + str(s.apell_alu),
            'cedula': str(s.tip_ced_alu) + " - "  + str(s.ced_alu),
            'foto': str(i.img) }
            acu+=1
        return JsonResponse(data)

class AlumnoDetailView(LoginRequiredMixin, DetailView):
    model = Account

    def get_context_data(self, **kwargs):
        context = super(AlumnoDetailView, self).get_context_data(**kwargs)
        context['vivienda'] = (Vivienda.objects.filter(alumno=self.object.pk)).first()
        context['fame']     = (Fame.objects.filter(alumno=self.object.pk)).first()
        alumno = Alumno_beca.objects.filter(alumno=self.object.pk).first()
        if alumno is not None:
            context['statu']    = (Acta.objects.filter(alumno=alumno.pk)).first()
        context['alumnoo']   = alumno
        return context

class AlumnoCreateView(CreateView):
    model = Account
    form_class = AlumnoModelForm

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail', args=(self.object.pk,))

class AlumnoCreateViewBeca(LoginRequiredMixin, CreateView):
    model = Alumno_beca
    form_class = AlumnoBecaForm

    def form_valid(self, form):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        print alumno
        _object = form.save(commit=False)
        _object.alumno = alumno
        self.object = _object.save()
        return super(AlumnoCreateViewBeca, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AlumnoCreateViewBeca, self).get_context_data(**kwargs)
        print self.kwargs['pk']
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        context['alumno'] = alumno
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],))

class AlumnoUpdateViewBeca(LoginRequiredMixin, UpdateView):
    model = Alumno_beca
    form_class = AlumnoBecaForm

    def get_context_data(self, **kwargs):
        context = super(AlumnoUpdateViewBeca, self).get_context_data(**kwargs)
        alumno = Alumno_beca.objects.filter(pk=self.kwargs['pk']).first()
        print alumno
        return context

    def get_success_url(self):
        alumno = Alumno_beca.objects.filter(pk=self.kwargs['pk']).first()
        print alumno
        return reverse_lazy('alumnoss:detail',args=(str(alumno.alumno.pk)))

class AlumnoDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('alumnoss:list')

class AlumnoUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AlumnoUpdateModelForm

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail', args=(self.object.pk,))

class ViviendaCreateView(LoginRequiredMixin, AlumnoFormValidMixin):
    model = Vivienda
    form_class = ViviendaModelForm

class ViviendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Vivienda
    form_class = ViviendaModelForm

    def get_context_data(self, **kwargs):
        context = super(ViviendaUpdateView, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumno
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.object.alumno.pk,))

class DatosFamiliarDetailView(LoginRequiredMixin, DetailView):
    model = models.Account
    template_name = "datos_familiar/datosfamiliar_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DatosFamiliarDetailView, self).get_context_data(**kwargs)
        context['familiar'] = (models.DatosFamiliar.objects.filter(alumno=self.object.pk))
        return context

class DatosFamiliarCreateView(LoginRequiredMixin, CreateView):
    model = models.DatosFamiliar
    form_class = DatosFamiliarModelForm

    def form_valid(self, form):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        _object = form.save(commit=False)
        _object.alumno = alumno
        self.object = _object.save()
        return super(DatosFamiliarCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DatosFamiliarCreateView, self).get_context_data(**kwargs)
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        context['alumno'] = alumno
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],))

class DatosFamiliarDeleteView(LoginRequiredMixin, DeleteView):
    model = models.DatosFamiliar

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.object.alumno.pk,))

class DatosFameCreateView(LoginRequiredMixin, FameFormValidMixin):
    model = Fame
    form_class = FameModelForm

class DatosFameUpdateView(LoginRequiredMixin, UpdateView):
    model = Fame
    form_class = FameModelForm

    def get_context_data(self, **kwargs):
        context = super(DatosFameUpdateView, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumno
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.object.alumno.pk,))
