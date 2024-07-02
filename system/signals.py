from django.dispatch import receiver
from django.db.models.signals import post_save
from system.models import Inscripciones, Notificaciones
@receiver(post_save, sender = Inscripciones)
def send_notification(sender, instance, **kwargs):
    Notificaciones.objects.create(
        texto="Nueva inscripcion al curso",
        curso=instance.curso_id  # Asigna el curso asociado a la inscripción
    )
    