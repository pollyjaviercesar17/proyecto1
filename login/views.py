# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, RedirectView, View
# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.decorators import login_required

class HomeTemplateView(TemplateView):
    template_name = 'login/home.html'


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, { 'form': form, 'message':'' })

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print username, password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.ced_alu is not None:
                    login(request, user)
                    #print user.pk
                    return redirect('/alumno/%i/detail' % (int(user.pk)))
                else:
                    login(request, user)
                    return redirect('/alumno/')
            else:
                return HttpResponse('no esta activo')
        else:
            mensaje= "Usuario o Contraseña Incorrecta"
            return render(request, self.template_name, {'form':self.form_class ,'message':mensaje })

class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('aja:panel-login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/') 

@login_required()
def Change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su Contraseña ha Sido Actualizada Sastifactoriamente!')
            return redirect('alumnoss:list')
        else:
            messages.error(request, 'Corrije el Error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/login_form.html', {
        'form': form
    })
