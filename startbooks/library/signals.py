from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Author, Book

@receiver(post_save, sender=Author)
def notify_new_autor(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "message": f"Novo autor cadastrado: {instance.name}"
            }
        )



@receiver(post_save, sender=Book)
def notify_new_book(sender, instance, created, **kwargs):
    author = instance.author
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "message": f"Autor {author.name} acaba de publicar: {instance.name}"
            }
        )
