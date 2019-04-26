# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# class based views.
from django.views.generic import ListView, TemplateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.core.urlresolvers import reverse_lazy, reverse

from alumno.models import Account, Alumno_beca
from vivienda.models import Vivienda
from fame.models import Fame
from datos_familiar.models import DatosFamiliar
from django.shortcuts import get_object_or_404
# Create your views here.
from datos_familiar import models
from acta import models, forms
from acta.mixins import *
from login.views import LoginRequiredMixin

class ActaCreateView(LoginRequiredMixin, ActaFormValidMixin):
    model = models.Acta
    form_class = forms.ActaForm


class ActaUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Acta
    form_class = forms.ActaForm

    def get_context_data(self, **kwargs):
        context = super(ActaUpdateView, self).get_context_data(**kwargs)
        alumno = Alumno_beca.objects.filter(pk=self.kwargs['pk']).first()
        return context

    def get_success_url(self):
        alumno = Alumno_beca.objects.filter(pk=self.kwargs['pk']).first()
        return reverse_lazy('alumnoss:detail',args=(str(alumno.alumno.pk)))

