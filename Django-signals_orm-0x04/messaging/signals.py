from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from messaging.models import Message, Notification, MessageHistory


@receiver(post_save, sender=Message)
def message_post_save_handler(sender, instance: Message, created, **kwargs):
    if created:
        new_notification = Notification.objects.create(
            user=instance.receiver,
            message=instance,
        )


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance: Message, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                edited_by = kwargs.get('user')
                MessageHistory.objects.create(
                    message=old_message, old_content=old_message.content, edited_by=edited_by)
                instance.edited = True
        except Message.DoesNotExist:
            pass
