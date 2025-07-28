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


class SweetModelTest(TestCase):
    def test_create_sweet(self):
        sweet = Sweet.objects.create(
            name='Gulab Jamun',
            description='Soft and juicy',
            category='Milk-based',
            price_per_kg=15.50,
            stock=50,
            image='sweets/gulabjamun.jpg',
            is_available=True,
            ingredients='Milk, Sugar, Cardamom',
            offer_percent=10,
            tags='popular,festival'
        )
        
        self.assertEqual(sweet.name, 'Gulab Jamun')
        self.assertEqual(sweet.price_per_kg, 15.50)
        self.assertEqual(sweet.stock, 50)
        self.assertTrue(sweet.is_available)
        self.assertEqual(sweet.offer_percent, 10)
        self.assertIn('festival', sweet.tags)
        self.assertIsNotNone(sweet.created_at)
        self.assertIsNotNone(sweet.updated_at)

    def test_create_sweet_offer_tags(self):
        sweet = Sweet.objects.create(
        name='Barfi',
        description='Milky and soft',
        category='Milk-based',
        price_per_kg=12.00,
        stock=30,
        offer_percent=15,
        tags='navratri,festival'
    )
        self.assertEqual(sweet.offer_percent, 15)
        self.assertIn('festival', sweet.tags)


# RED - Fails initially because we don't have total_price logic updated or sweet.stock not updated

def test_purchase_logic(self):
    # Create a Purchase and expect total_price = quantity * price_per_kg
    purchase = Purchase.objects.create(user=self.user, sweet=self.sweet, quantity=3)
    self.assertEqual(purchase.total_price, 30)  # Fails if total_price not auto-calculated
    self.assertEqual(purchase.sweet.stock, 97)  # Fails if stock not auto-decreased


class PurchaseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.sweet = Sweet.objects.create(
            name='Rasgulla',
            description='Delicious sweet',
            category='Milk-based',
            price_per_kg=10.00,
            stock=100,
            is_available=True
        )

    def test_purchase_logic(self):
        quantity = 3
        expected_price = quantity * float(self.sweet.price_per_kg)
        expected_stock = self.sweet.stock - quantity

        purchase = Purchase.objects.create(user=self.user, sweet=self.sweet, quantity=quantity)

        self.assertEqual(float(purchase.total_price), expected_price)
        self.sweet.refresh_from_db()
        self.assertEqual(self.sweet.stock, expected_stock)
    
