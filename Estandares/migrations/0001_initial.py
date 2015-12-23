# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=100)),
                ('tematica', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('fechaPublicacion', models.DateField()),
                ('vigencia', models.DateField()),
                ('otrasVersiones', models.CharField(max_length=100)),
                ('discusion', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioConsulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contibuidor', models.CharField(max_length=200)),
                ('institucion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=200)),
                ('comentario', models.TextField()),
                ('codigo', models.ForeignKey(to='Estandares.Documento')),
            ],
        ),
        migrations.CreateModel(
            name='Versiones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('url', models.CharField(max_length=250)),
                ('codigo', models.ManyToManyField(to='Estandares.Documento')),
            ],
        ),
    ]
