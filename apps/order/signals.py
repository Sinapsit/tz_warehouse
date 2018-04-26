from order.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Order)
def save_order(sender, instance, **kwargs):
    print(kwargs.keys())

