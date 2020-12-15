# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('cedula', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('nombre', models.CharField(max_length=150)),
                ('segundo_nombre', models.CharField(max_length=150, blank=True)),
                ('apellido', models.CharField(max_length=150)),
                ('segundo_apellido', models.CharField(max_length=150, blank=True)),
                ('sexo', models.CharField(max_length=20, choices=[('M', 'masculino'), ('F', 'femenino')])),
                ('num_contacto', models.IntegerField(blank=True, null=True)),
                ('representante', models.CharField(max_length=150, blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=150, choices=[('A', 'Activo'), ('I', 'Inactivo')])),
                ('nota_memo', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('apellido', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=1000, blank=True, null=True)),
                ('status', models.CharField(max_length=150, choices=[('A', 'Activo'), ('I', 'Inactivo')])),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Clase_Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('clase', models.ForeignKey(blank=True, null=True, to='academica.Clase')),
            ],
            options={
                'verbose_name': 'Profesor de Clase',
                'verbose_name_plural': 'Profesores de cada clase',
                'ordering': ('profesor',),
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ano_lectivo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('status', models.CharField(max_length=150, choices=[('A', 'Activo'), ('I', 'Inactivo')])),
                ('alumno', models.ForeignKey(to='academica.Alumno')),
            ],
            options={
                'verbose_name': 'matrícula',
                'verbose_name_plural': 'matrículas',
                'ordering': ('alumno',),
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'niveles',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('valor', models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)),
                ('tipo', models.CharField(max_length=150)),
                ('publicada', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(to='academica.Alumno')),
                ('clase', models.ForeignKey(to='academica.Clase')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=250, blank=True)),
                ('num_contacto', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=150, choices=[('A', 'Activo'), ('I', 'Inactivo')])),
                ('nota_memo', models.TextField(blank=True)),
                ('nivel', models.ForeignKey(blank=True, null=True, to='academica.Nivel')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil de profesor',
                'verbose_name_plural': 'perfiles de profesores',
                'ordering': ('-usuario',),
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ano_lectivo', models.CharField(max_length=150, blank=True)),
                ('quimestre', models.IntegerField()),
                ('parcial', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='periodo',
            field=models.ForeignKey(to='academica.Periodo'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='nivel',
            field=models.ForeignKey(null=True, to='academica.Nivel'),
        ),
        migrations.AddField(
            model_name='clase_profesor',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, to='academica.Perfil_Profesor'),
        ),
        migrations.AddField(
            model_name='clase',
            name='nivel',
            field=models.ForeignKey(to='academica.Nivel'),
        ),
    ]
