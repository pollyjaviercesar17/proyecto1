# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-13 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('acta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acta',
            name='alumno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno_beca'),
        ),
    ]
