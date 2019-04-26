# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from alumno.models import Alumno_beca

# Create your models here.

class Acta(models.Model):
	alumno= models.OneToOneField(Alumno_beca)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.alumno)
