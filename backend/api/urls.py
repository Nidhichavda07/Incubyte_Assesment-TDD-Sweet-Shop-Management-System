from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterUser,
    Dashboard,
    SweetViewSet,
    SweetDetailView,
    PurchaseViewSet,
    PurchaseSweetView,
    PurchaseListView,
)

# Router for ViewSets
router = DefaultRouter()
router.register(r'sweets', SweetViewSet, basename='sweet')
router.register(r'purchases', PurchaseViewSet, basename='purchase')


# URL patterns
urlpatterns = [
    # Authentication
    path('admin/', admin.site.urls),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Dashboard
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # Sweet detail (not using ViewSet for this one)
    path('sweets/<int:pk>/', SweetDetailView.as_view(), name='sweet-detail'),

    # Purchase a specific sweet
    path('sweets/<int:sweet_id>/purchase/', PurchaseSweetView.as_view(), name='purchase-sweet'),

    # Purchase list view
    path('purchase-list/', PurchaseListView.as_view(), name='purchase-list'),

    # Include all ViewSet routes
    path('', include(router.urls)),
]
