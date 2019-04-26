from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
# models
from alumno.models import Account, Alumno_beca
from acta import models

class ActaFormValidMixin(CreateView):

    def get(self, request, *args, **kwargs):    
        beca = get_object_or_404(Alumno_beca, alumno=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=beca):
            return super(ActaFormValidMixin, self).get(request, *args, **kwargs)
        else: return redirect(reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],)))


    def form_valid(self, form):
        beca = get_object_or_404(Alumno_beca, alumno=self.kwargs['pk'])
        if not self.model.objects.filter(alumno=beca):
            _object = form.save(commit=False)
            _object.alumno = beca
            self.object = _object.save()
            return super(ActaFormValidMixin, self).form_valid(form)
        else: return HttpResponseNotFound('Este alumno ya esta aprobado')

    def get_context_data(self, **kwargs):
        context = super(ActaFormValidMixin, self).get_context_data(**kwargs)
        context['alumno'] = self.object.alumno if self.object else None
        return context

    def get_success_url(self):
        return reverse_lazy('alumnoss:detail',args=(self.kwargs['pk'],))