from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item

class ItemTests(APITestCase):
    def test_create_item(self):
        """
        Ensure we can create a new item.
        """
        url = reverse('item-list')
        data = {'name': 'Test Item', 'description': 'A test item', 'category': 'Test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
