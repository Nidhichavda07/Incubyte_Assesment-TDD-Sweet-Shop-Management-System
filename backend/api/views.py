from rest_framework import status, viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Sweet, Purchase
from .serializers import UserSerializer, SweetSerializer, PurchaseSerializer


# ---------------------------
# Auth & User Views
# ---------------------------

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Welcome {request.user.username} to your dashboard!"})


# ---------------------------
# Sweet Views
# ---------------------------

class SweetViewSet(viewsets.ModelViewSet):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)


class SweetListCreateView(generics.ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sweet_list(request):
    sweets = Sweet.objects.filter(is_available=True)
    serializer = SweetSerializer(sweets, many=True)
    return Response(serializer.data)


class SweetListView(generics.ListAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [IsAuthenticated]


# ---------------------------
# Purchase Views
# ---------------------------

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PurchaseListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)

class PurchaseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PurchaseCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        sweet_id = request.data.get('sweet')
        quantity = int(request.data.get('quantity', 0))

        sweet = get_object_or_404(Sweet, id=sweet_id)

        if quantity <= 0:
            return Response({"error": "Quantity must be positive."}, status=status.HTTP_400_BAD_REQUEST)
        if sweet.stock < quantity:
            return Response({"error": f"Only {sweet.stock} in stock."}, status=status.HTTP_400_BAD_REQUEST)

        purchase = Purchase.objects.create(
            user=user,
            sweet=sweet,
            quantity=quantity,
            total_price=sweet.price_per_kg * quantity
        )

        sweet.stock -= quantity
        sweet.save()

        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PurchaseSweetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, sweet_id):
        sweet = get_object_or_404(Sweet, id=sweet_id)
        quantity = int(request.data.get("quantity", 1))

        if sweet.stock < quantity:
            return Response({"error": "Not enough stock."}, status=status.HTTP_400_BAD_REQUEST)

        total_price = sweet.price_per_kg * quantity

        Purchase.objects.create(
            user=request.user,
            sweet=sweet,
            quantity=quantity,
            total_price=total_price
        )

        sweet.stock -= quantity
        sweet.save()

        return Response({"message": "Purchase successful."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_purchase(request):
    sweet_id = request.data.get('sweet_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        sweet = Sweet.objects.get(id=sweet_id)
        purchase = Purchase.objects.create(
            user=request.user,
            sweet=sweet,
            quantity=quantity,
            total_price=sweet.price_per_kg * quantity
        )
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data, status=201)
    except Sweet.DoesNotExist:
        return Response({'error': 'Sweet not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_purchases(request):
    purchases = Purchase.objects.filter(user=request.user).order_by('-purchased_at')
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_purchases(request):
    purchases = Purchase.objects.filter(user=request.user).select_related('sweet')
    data = [
        {
            'sweet_name': p.sweet.name,
            'price': p.sweet.price_per_kg,
            'quantity': p.quantity,
            'total_price': p.total_price,
            'purchased_at': p.purchased_at,
        }
        for p in purchases
    ]
    return Response(data)
