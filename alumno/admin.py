from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import admin
from alumno.models import Account, Alumno_beca
from vivienda import models 
from datos_familiar.models import DatosFamiliar
from fame.models import Fame
# Register your models here.


admin.site.register(Alumno_beca)

class ViviendaInLine(admin.StackedInline):
	model = models.Vivienda
	extra = 1


class DatosFamiliarInLine(admin.StackedInline):
	model = DatosFamiliar
	extra = 2
	raw_id_fields = ('alumno',)

class FameInLine(admin.StackedInline):
	model =Fame
	extra = 1

#class imgInLine(admin.StackedInline):
#	model = img
#	extra = 1
		

@admin.register(Account)
class AlumnoAdmin(admin.ModelAdmin):
	inlines = [ViviendaInLine, DatosFamiliarInLine, FameInLine]
	