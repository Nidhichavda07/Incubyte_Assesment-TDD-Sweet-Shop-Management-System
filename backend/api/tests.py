from django.test import TestCase
from django.contrib.auth.models import User
from .models import Sweet, Purchase
from rest_framework.test import APIClient
from rest_framework import status

class PurchaseAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.sweet = Sweet.objects.create(
            name='Rasgulla',
            description='Delicious sweet',
            category='Milk-based',
            price_per_kg=10,
            stock=100,
            is_available=True
        )

    def test_create_purchase(self):
        purchase = Purchase.objects.create(user=self.user, sweet=self.sweet, quantity=2)
        self.assertEqual(purchase.total_price, 20)
        self.assertEqual(purchase.sweet.stock, 98)


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/register/'

    def test_user_registration_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserLoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = '/api/token/'
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_successful(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_with_wrong_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
