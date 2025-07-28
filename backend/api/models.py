# models.py

from django.db import models
from django.contrib.auth.models import User

class Sweet(models.Model):
    """
    Represents a sweet item available for purchase.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    price_per_kg = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='sweets/')
    is_available = models.BooleanField(default=True)
    ingredients = models.TextField(blank=True, null=True)
    offer_percent = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.sweet.price_per_kg
        self.sweet.stock -= self.quantity
        self.sweet.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} purchased {self.quantity} x {self.sweet.name}"
