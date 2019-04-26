# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-13 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tip_ced_alu', models.CharField(choices=[(b'', b'Nacionalidad'), (b'V', b'V'), (b'E', b'E')], max_length=2, verbose_name='NACIONALIDAD')),
                ('ced_alu', models.IntegerField(null=True, unique=True, verbose_name='CEDULA')),
                ('nom_alu', models.CharField(blank=True, max_length=45, null=True, verbose_name='NOMBRE')),
                ('apell_alu', models.CharField(blank=True, max_length=45, null=True, verbose_name='APELLIDO')),
                ('fech_naci_alu', models.DateField(blank=True, null=True, verbose_name='FECHA DE NACIMIENTO')),
                ('tlf_cel_alu', models.IntegerField(blank=True, null=True, verbose_name='CELULAR')),
                ('tlf_fijo_alu', models.IntegerField(blank=True, null=True, verbose_name='TELEFONO FIJO')),
                ('email_alu', models.EmailField(blank=True, max_length=254, null=True, verbose_name='CORREO')),
                ('carrera', models.CharField(choices=[(b'', b'CARRERA'), (b'PNF INFORMATICA', b'PNF INFORMATICA'), (b'PNF AGROALIMENTARIA', b'PNF AGROALIMENTARIA'), (b'PNF ELECTRICA', b'PNF ELECTRICA'), (b'PNF MECANICA', b'PNF MECANICA'), (b'PNF SEGURIDAD ALIMENTARIA', b'PNF SEGURIDAD ALIMENTARIA'), (b'PNF ADMINISTRACION', b'PNF ADMINISTRACION')], max_length=20, verbose_name='CARRERA')),
                ('trayecto', models.CharField(choices=[(b'', b'TRAYECTO'), (b'I', b'I'), (b'II', b'II'), (b'III', b'III'), (b'IV', b'IV')], max_length=20, verbose_name='TRAYECTO')),
                ('semestre', models.CharField(choices=[(b'', b'SEMESTRE'), (b'I', b'I'), (b'II', b'II'), (b'III', b'III'), (b'IV', b'IV'), (b'V', b'V'), (b'VI', b'VI'), (b'VII', b'VII'), (b'VIII', b'VIII')], max_length=20, verbose_name='SEMESTRE')),
                ('direccion', models.TextField(blank=True, null=True, verbose_name='DIRECCION')),
                ('punto_ref', models.TextField(blank=True, null=True, verbose_name='PUNTO DE REFERENCIA')),
                ('procedencia', models.TextField(blank=True, null=True, verbose_name='PROCEDENCIA')),
                ('username', models.CharField(max_length=40, unique=True, verbose_name='USERNAME')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alumno_beca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vive_resid', models.BooleanField(default=False, verbose_name='VIVE RESIDENCIADO')),
                ('viaja_clase', models.BooleanField(default=False, verbose_name='VIAJA A CLASE')),
                ('tiempo_viaje', models.TimeField(blank=True, null=True, verbose_name='TIEMPO DE VIAJE')),
                ('gasto_viaje', models.IntegerField(blank=True, null=True, verbose_name='GASTO DE VIAJE')),
                ('turno', models.CharField(choices=[(b'', b'Turno'), (b'DIURNO', b'DIURNO'), (b'NOCHE', b'NOCTURNO')], max_length=20, verbose_name='TURNO')),
                ('ira', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Indice de Rendimiento Academico')),
                ('tipo_beca', models.CharField(blank=True, max_length=40, null=True, verbose_name='TIPO DE BECA')),
                ('img', models.ImageField(blank=True, upload_to='tipo_carnet')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
