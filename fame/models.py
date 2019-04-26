# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
# Create your models here.

from alumno.models import Account


class Fame(models.Model):
	tipo_solicitud = models.CharField(max_length=500, blank=True, null=True)
	constancia = models.FileField(blank=True, upload_to='anexo_costancia')
	presupuesto = models.FileField(blank=True, upload_to='anexo_presupuesto')
	alumno = models.ForeignKey(Account)





