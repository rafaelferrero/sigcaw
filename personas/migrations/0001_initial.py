# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-01 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Foto Carnet')),
                ('numero_credencial', models.CharField(max_length=255, unique=True, verbose_name='Número de Credencial')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('estado_civil', models.CharField(choices=[('Casado', 'Casado/a'), ('Soltero', 'Soltero/a'), ('Divorciado', 'Divorciado/a'), ('Viudo', 'Viudo/a'), ('Concubino', 'Concubino/a')], default='Casado', max_length=255, verbose_name='Estado Civil')),
                ('lugar_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad', verbose_name='Lugar de Nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionAnual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.IntegerField(unique=True, verbose_name='Año')),
                ('puntaje_en_numero', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Puntaje Numérico')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero_calificacion', to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name_plural': 'Calificaciones Anuales',
                'verbose_name': 'Calificación Anual',
            },
        ),
        migrations.CreateModel(
            name='DireccionElectronica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Direcciones de Email',
                'verbose_name': 'Direccion de Email',
            },
        ),
        migrations.CreateModel(
            name='DireccionPostal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('calle', models.CharField(max_length=255, verbose_name='Calle')),
                ('numero', models.SmallIntegerField(verbose_name='Número')),
                ('piso', models.CharField(blank=True, max_length=5, null=True, verbose_name='Piso')),
                ('departamento', models.CharField(blank=True, max_length=5, null=True, verbose_name='Departamento')),
            ],
            options={
                'verbose_name_plural': 'Direcciones Postales',
                'verbose_name': 'Dirección Postal',
            },
        ),
        migrations.CreateModel(
            name='DireccionWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('direccion', models.URLField(verbose_name='Dirección Web')),
                ('tipo', models.CharField(choices=[('S', 'Perfil Web Social'), ('L', 'Pagina Web Laboral')], default='S', max_length=255, verbose_name='Tipo web')),
            ],
            options={
                'verbose_name_plural': 'Direcciones Web',
                'verbose_name': 'Dirección Web',
            },
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título o cargo')),
                ('periodo_desde', models.DateField(verbose_name='Fecha de Inicio')),
                ('periodo_hasta', models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name_plural': 'Empleos',
                'verbose_name': 'Empleo',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuit', models.CharField(choices=[('CUIT', 'CUIT'), ('CUIL', 'CUIL')], default='CUIT', max_length=4, verbose_name='CUIT/CUIL')),
                ('nro_cuit', models.CharField(blank=True, max_length=13, null=True, verbose_name='Numero de CUIT/CUIL')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[('P', 'Primario'), ('S', 'Secundario'), ('T', 'Terciario'), ('U', 'Universitario')], default='P', max_length=5, verbose_name='Nivel de Estudio')),
                ('estado', models.CharField(choices=[('F', 'Finalizado'), ('C', 'Cursando'), ('A', 'Abandonado')], default='F', max_length=5, verbose_name='Estado de cursado')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('periodo_desde', models.DateField(verbose_name='Fecha de Inicio')),
                ('periodo_hasta', models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name_plural': 'Estudios',
                'verbose_name': 'Estudio',
            },
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(choices=[('Hermano', 'Hermano/a'), ('Padre', 'Padre'), ('Madre', 'Madre'), ('Hijo', 'Hijo/a'), ('Abuelo', 'Abuelo/a'), ('Nieto', 'Nieto/a'), ('Tio', 'Tío/a'), ('Primo', 'Primo/a'), ('Esposo', 'Esposo/a')], default='Hermano', max_length=255, verbose_name='Parentesco')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombero', to='personas.Bombero', verbose_name='Bombero')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso', models.CharField(choices=[('P', 'Particular'), ('L', 'Laboral')], default='P', max_length=255, verbose_name='Uso')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Obervaciones')),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Teléfono')),
                ('tipo', models.CharField(choices=[('C', 'Celular'), ('F', 'Fijo')], default='C', max_length=255, verbose_name='Tipo de Teléfono')),
            ],
            options={
                'verbose_name_plural': 'Teléfonos',
                'verbose_name': 'Teléfono',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Entidad')),
                ('razon_social', models.CharField(max_length=255, verbose_name='Razón Social')),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'verbose_name': 'Institución',
            },
            bases=('personas.entidad',),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('entidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Entidad')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE')], default='DNI', max_length=10, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=11, unique=True, verbose_name='Número de documento')),
                ('grupo_sanguineo', models.CharField(choices=[('AB', 'Grupo AB'), ('A', 'Grupo A'), ('B', 'Grupo B'), ('O', 'Grupo O')], default='AB', max_length=255, verbose_name='Grupo Sanguíneo')),
                ('factor_sanguineo', models.CharField(choices=[('+', 'RH+'), ('-', 'RH-')], default='+', max_length=255, verbose_name='Factor Sanguíneo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('fecha_desceso', models.DateField(blank=True, null=True, verbose_name='Fecha de Fallecimiento')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
                'verbose_name_plural': 'Personas',
                'verbose_name': 'Persona',
            },
            bases=('personas.entidad',),
        ),
        migrations.AddField(
            model_name='telefono',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionweb',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionpostal',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='direccionpostal',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad', verbose_name='Localidad'),
        ),
        migrations.AddField(
            model_name='direccionelectronica',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Entidad'),
        ),
        migrations.AddField(
            model_name='parentesco',
            name='familiar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='personas.Persona', verbose_name='Familiar'),
        ),
        migrations.AddField(
            model_name='estudio',
            name='establecimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Establecimiento'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='bombero',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bombero', to='personas.Persona', verbose_name='Persona'),
        ),
    ]
