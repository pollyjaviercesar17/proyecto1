from django import forms
from django.forms.widgets import TextInput
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from alumno.models import Account, Alumno_beca
from aparte.forms_date import DateInput, TimeInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#choices
from aparte.select import Selects


class AlumnoModelForm(UserCreationForm):
    class Meta:
        model = Account
        exclude = ('is_active', 'date_joined', 'is_superuser', 'last_login',
            'created_at', 'updated_at', 'groups', 'user_permissions', 'password', 'is_staff')
        widgets = {
            'fech_naci_alu': DateInput(format = '%Y-%m-%d'),
            'tiempo_viaje': TimeInput(format = '%H-%M'),
        }



class AlumnoUpdateModelForm(UserChangeForm):
    class Meta:
        model = Account
        exclude = ('username','is_active', 'date_joined', 'is_superuser', 'last_login',
            'created_at', 'updated_at', 'groups', 'user_permissions', 'is_staff',)
        widgets = {
            'fech_naci_alu': DateInput(format = '%Y-%m-%d'),
            'tiempo_viaje': TimeInput(format = '%H-%M'),
        }


class AlumnoBecaForm(forms.ModelForm):
    class Meta:
        model = Alumno_beca
        exclude = ('created_at', 'updated_at','alumno',)
        widgets = {
            'fech_naci_alu': DateInput(format = '%Y-%m-%d'),
            'tiempo_viaje': TimeInput(format = '%H-%M'),
        }