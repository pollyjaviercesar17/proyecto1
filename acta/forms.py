from django import forms 
from acta import models


class ActaForm(forms.ModelForm):
    class Meta:
        model = models.Acta
        exclude = ('created_at', 'updated_at', 'alumno')
