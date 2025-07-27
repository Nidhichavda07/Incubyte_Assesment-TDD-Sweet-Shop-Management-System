# admin.py

from django.contrib import admin
from .models import Sweet, Purchase


@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    """
    Admin configuration for Sweet model.
    """
    list_display = ('name', 'category', 'price_per_kg', 'stock', 'is_available')
    search_fields = ('name', 'category', 'ingredients', 'tags')
    list_filter = ('category', 'is_available')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    """
    Admin configuration for Purchase model.
    """
    list_display = ('user', 'sweet', 'quantity', 'total_price', 'purchased_at')
    search_fields = ('user__username', 'sweet__name')
    list_filter = ('purchased_at',)
    readonly_fields = ('total_price', 'purchased_at')
