import requests
from order.models import Order


class BaseConnector(object):
    def __init__(self, instance):
        self.server_url = 'http://localhost:8000'
        self.instance_id = instance

    def sync_status(self):
        order = Order.objects.get(number=self.instance_id)
        data = self.get_serializer(order)
        data_status = data['status']
        url = f'{self.server_url}/order/item/{self.instance_id}'
        resp = requests.patch(url, data=data_status)

    def create_order(self):
        url = f'{self.server_url}/order/create/'
        order = Order.objects.get(number=self.instance_id)
        data = self.get_serializer(order)
        resp = requests.post(url, data=data)

    @staticmethod
    def get_serializer(instance):
        from order.serializers import OrderSerializer
        serializer = OrderSerializer(instance)
        return serializer.data
