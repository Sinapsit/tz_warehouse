from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from order.models import Order


class OrderTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("\nStart test order app")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("End test order app\n")

    def setUp(self):
        user = get_user_model().objects.create_user('Jon Dow', password='Jon42dow')
        Order.objects.create(
            **{
                "created": "2018-04-26T10:54:04.541456Z",
                "modified": "2018-04-26T10:54:04.541897Z",
                "number": "65496868",
                "currency": "RUB",
                "status": "order",
                "total_incl_tax": "45.00",
                "total_excl_tax": "56.00",
                "shipping_incl_tax": "67.00",
                "shipping_excl_tax": "78.00",
                "user": user
            }
        )

    def test_order_exist(self):
        """Order model exist"""
        order = Order.objects.get(number="65496868")
        self.assertEqual(order.number, "65496868")
