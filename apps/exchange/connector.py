import requests
from order.models import Order


class BaseConnector(object):
    def __init__(self, instance, server_url):
        self.server_url = server_url
        self.instance = Order.objects.get(id=instance)

    def sync_status(self):
        data = self.get_serializer(self.instance)
        data_status = {
            'status': data['status'],
        }
        url = f'{self.server_url}/order/item/{self.instance.number}/'
        self.send(url, data_status)

    def create_order(self):
        url = f'{self.server_url}/order/create/'
        data = self.get_serializer(self.instance)
        for i in ['id', 'synced']:
            del data[i]
        self.send(url, data)

    def send(self, url, data,):
        resp = requests.post(url, data=data)
        if resp.status_code == 200 or resp.status_code == 201:
            self.instance.synced = True
        else:
            self.instance.synced = False
        self.instance.save()

    @staticmethod
    def get_serializer(instance):
        from order.serializers import OrderSerializer
        serializer = OrderSerializer(instance)
        return serializer.data
