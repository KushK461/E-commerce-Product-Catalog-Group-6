from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {'name': 'Test Product', 'description': 'A test product', 'price': '99.99'}
        self.response = self.client.post('/api/products/', self.product_data)

    def test_create_product(self):
        self.assertEqual(self.response.status_code, 201)
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.description, 'A test product')
        self.assertEqual(product.price, 99.99)
