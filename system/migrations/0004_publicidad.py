# Generated by Django 5.0.4 on 2024-06-17 20:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_cursos_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(upload_to='system/images/publicidad/', verbose_name='Imagen')),
                ('nombre_boton', models.CharField(default='Leer más', max_length=30, verbose_name='Nombre del Botón')),
                ('url_boton', models.URLField(blank=True, default='#', verbose_name='URL Boton')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
    ]
