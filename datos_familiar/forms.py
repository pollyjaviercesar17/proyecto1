from django import forms
from datos_familiar.models import DatosFamiliar
from aparte.forms_date import DateInput, TimeInput

class DatosFamiliarModelForm(forms.ModelForm):
    class Meta:
        model = DatosFamiliar
        exclude = ('alumno',)
        widgets = {
            'fecha_naci': DateInput(format = '%Y-%m-%d'),
            
        }
