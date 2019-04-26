from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
# models
from alumno import models
from vivienda import models

class AlumnoFormValidMixin(CreateView):

    def get(self, request, *args, **kwargs):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=alumno):
            return super(AlumnoFormValidMixin, self).get(request, *args, **kwargs)
        else: return redirect(reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],)))


    def form_valid(self, form):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=alumno):
            _object = form.save(commit=False)
            _object.alumno = alumno
            self.object = _object.save()
            return super(AlumnoFormValidMixin, self).form_valid(form)
        else: return HttpResponseNotFound('Este alumno ya tiene vivienda registrada')

    def get_context_data(self, **kwargs):
        context = super(AlumnoFormValidMixin, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumno if self.object else None
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],))


class FameFormValidMixin(CreateView):

    def get(self, request, *args, **kwargs):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=alumno):
            return super(FameFormValidMixin, self).get(request, *args, **kwargs)
        else: return redirect(reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],)))


    def form_valid(self, form):
        alumno = get_object_or_404(models.Account, pk=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=alumno):
            _object = form.save(commit=False)
            _object.alumno = alumno
            self.object = _object.save()
            return super(FameFormValidMixin, self).form_valid(form)
        else: return HttpResponseNotFound('Este alumno ya tiene fame registrado')

    def get_context_data(self, **kwargs):
        context = super(FameFormValidMixin, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumno if self.object else None
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],))
        