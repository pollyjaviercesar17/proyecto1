# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils import timezone
#from pas.thumbs import ImageWithThumbsField

#choices
from aparte.select import Selects

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Usuario Debe Tener Un Username Valido.')
        account = self.model(
            username=self.model.normalize_username(username)
        )
        account.set_password(password)
        account.save()
        return account
    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account

class Account(AbstractBaseUser, PermissionsMixin):
    tip_ced_alu = models.CharField(_('NACIONALIDAD'), max_length=2, choices=Selects().nacionali())
    ced_alu = models.IntegerField(_('CEDULA'), null=True, unique=True )
    nom_alu = models.CharField(_('NOMBRE'), max_length=45, null=True, blank=True)
    apell_alu = models.CharField(_('APELLIDO'),max_length=45, null=True, blank=True)
    fech_naci_alu = models.DateField(_('FECHA DE NACIMIENTO'), null=True, blank=True )
    tlf_cel_alu = models.IntegerField(_('CELULAR'), null=True, blank=True)
    tlf_fijo_alu = models.IntegerField(_('TELEFONO FIJO'), null=True, blank=True)
    email_alu = models.EmailField(_('CORREO'), null=True, blank=True)

    carrera = models.CharField(_('CARRERA'), max_length=20, choices=Selects().carrera())
    trayecto = models.CharField(_('TRAYECTO'),max_length=20, choices=Selects().trayecto())
    semestre = models.CharField(_('SEMESTRE'),max_length=20, choices=Selects().semestre())

    username = models.CharField(_('USERNAME'), max_length=40, null=False, unique=True, blank=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    direccion = models.TextField(_('DIRECCION'), blank = True, null=True)
    punto_ref = models.TextField(_('PUNTO DE REFERENCIA'), blank = True, null=True)
    procedencia = models.TextField(_('PROCEDENCIA'), blank=True, null=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.ced_alu)

    def get_full_name(self):
        return ' '.join([str(self.nom_alu), ' ', str(self.apell_alu)]).encode('utf-8').strip()

    def get_short_name(self):
        return str(self.nom_alu)


class Alumno_beca(models.Model):
	vive_resid = models.BooleanField(_('VIVE RESIDENCIADO'), default=False)
	viaja_clase = models.BooleanField(_('VIAJA A CLASE'), default=False)
	tiempo_viaje = models.TimeField(_('TIEMPO DE VIAJE'), null=True, blank=True)
	gasto_viaje = models.IntegerField(_('GASTO DE VIAJE'), blank=True, null=True)
	turno = models.CharField(_('TURNO'),max_length=20, choices=Selects().turno())
	ira = models.DecimalField(_('Indice de Rendimiento Academico'), decimal_places= 2, max_digits=10, blank=True, null=True)
	tipo_beca = models.CharField(_('TIPO DE BECA'), max_length=40, null=True, blank=True)
	img = models.ImageField(blank=True, upload_to='tipo_carnet')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	alumno = models.ForeignKey(Account)
