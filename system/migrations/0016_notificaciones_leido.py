# Generated by Django 5.0.4 on 2024-06-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_notificaciones_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificaciones',
            name='leido',
            field=models.BooleanField(default=False),
        ),
    ]