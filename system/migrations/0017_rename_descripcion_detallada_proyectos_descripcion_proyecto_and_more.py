# Generated by Django 5.0.4 on 2024-07-02 00:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_notificaciones_leido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectos',
            old_name='descripcion_detallada',
            new_name='descripcion_proyecto',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='descripcion_corta',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ImagenProyectos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='system/images/proyectos/')),
                ('servicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='system.proyectos')),
            ],
        ),
    ]
