from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
import json


class MenuViewTest(TestCase):
    def setUp(self):

        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword123')
        self.client.force_authenticate(user=self.user)

        self.menu1 = Menu.objects.create(
            title="Menu 1", price=9.99, inventory=10)
        self.menu2 = Menu.objects.create(
            title="Menu 2", price=19.99, inventory=20)
        self.menu3 = Menu.objects.create(
            title="Menu 3", price=29.99, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_response = [
            {'id': self.menu1.id, 'title': self.menu1.title,
                'price': f"{self.menu1.price}", 'inventory': self.menu1.inventory},
            {'id': self.menu2.id, 'title': self.menu2.title,
                'price': f"{self.menu2.price}", 'inventory': self.menu2.inventory},
            {'id': self.menu3.id, 'title': self.menu3.title,
                'price': f"{self.menu3.price}", 'inventory': self.menu3.inventory},
        ]

        response_data = json.loads(response.content)

        self.assertEqual(response_data, expected_response)
