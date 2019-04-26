from django import forms
from django.forms.widgets import TextInput
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from vivienda.models import  Vivienda


class ViviendaModelForm(forms.ModelForm):
    class Meta:
        model = Vivienda 
        fields =[
            #vivienda
            'tipo_vivienda',

            #tenencia de la vivienda
            'tenencia_vivienda',

            #distribucion espacial
            'num_dormitorio',
            'sala_di',
            'cocina_di',
            'comedor_di',
            'bano_di',
            'lavadero_di',
            'patio_di',
            'garaje_di',
            'jardin_di',

            #equipamiento de la vivienda
            'nevera_eq',
            'cocina_eq',
            'tv_eq',
            'dvd_eq',
            'ventiladores_eq',
            'a_a_eq',
            'computadora_eq',
            'lavadora_eq',
            'recibo_eq',
            'comedor_eq',
            'camas_eq',

            #servicios
            'agua_se',
            'red_cloacas_se',
            'electricidad_se',
            'internet_se',
            'tv_cable_se',
            'telefono_se',
            'trans_publico_se',
            'aseo_urba_se',

                ]
     


