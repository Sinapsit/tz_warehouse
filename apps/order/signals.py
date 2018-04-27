from order.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver
from exchange.connector import BaseConnector
from configuration.models import RemoteServer


@receiver(post_save, sender=Order)
def save_order(sender, instance, **kwargs):
    server = RemoteServer.get_solo()
    if server.url:
        connector = BaseConnector(instance.id)
        if kwargs["created"]:
            pass
            # connector.create_order()
        else:
            connector.sync_status()


