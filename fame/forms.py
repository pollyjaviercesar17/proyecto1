from django import forms

from fame import models

class FameModelForm(forms.ModelForm):
	class Meta:
		model= models.Fame
		fields=('tipo_solicitud', 'constancia', 'presupuesto')