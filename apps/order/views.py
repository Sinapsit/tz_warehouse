from rest_framework import generics
from order import models, serializers


class OrderListView(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderItemView(generics.RetrieveUpdateAPIView):
    lookup_field = 'number'
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()