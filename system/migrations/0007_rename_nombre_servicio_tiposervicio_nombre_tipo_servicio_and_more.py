# Generated by Django 5.0.4 on 2024-06-18 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_tiposervicio_servicios_servicio_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiposervicio',
            old_name='nombre_servicio',
            new_name='nombre_tipo_servicio',
        ),
        migrations.AlterField(
            model_name='servicios',
            name='servicio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.tiposervicio', verbose_name='Seleciones un tipo de servicio'),
        ),
    ]
