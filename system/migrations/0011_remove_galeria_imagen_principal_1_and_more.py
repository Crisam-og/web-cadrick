# Generated by Django 5.0.4 on 2024-06-26 23:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_servicios_imagen_delete_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='imagen_principal_1',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='imagen_principal_2',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='imagen_principal_3',
        ),
        migrations.CreateModel(
            name='ImagenGaleria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('imagen', models.ImageField(upload_to='system/images/galeria/')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='system.galeria')),
            ],
        ),
    ]