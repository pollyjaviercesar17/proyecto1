# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-18 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='num_dormitorio',
            field=models.IntegerField(default=0, verbose_name='Numero de dormitorios'),
        ),
    ]
