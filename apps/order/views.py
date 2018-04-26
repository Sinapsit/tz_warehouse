from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import Response
from order import models, serializers


class OrderListView(ListAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderCreateView(CreateAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderItemView(RetrieveUpdateAPIView):
    lookup_field = 'number'
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()