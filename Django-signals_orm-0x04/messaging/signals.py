from django.db.models.signals import post_save
from django.dispatch import receiver
from messaging.models import Message, Notification


@receiver(post_save, sender=Message)
def message_post_save_handler(sender, instance: Message, created, **kwargs):
    if created:
        new_notification = Notification.objects.create(
            user=instance.receiver,
            message=instance,
        )
