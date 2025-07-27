# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer

# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class Dashboard(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({
#             "message": f"Welcome {request.user.username} to your dashboard!"
#         })

# from rest_framework import viewsets, permissions
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Sweet
# from .serializers import SweetSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def sweet_list(request):
#     sweets = Sweet.objects.filter(is_available=True)
#     serializer = SweetSerializer(sweets, many=True, context={'request': request})
#     return Response(serializer.data)

# # api/views.py

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import ListAPIView
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetListView(ListAPIView):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticated]

# # views.py (using Django REST Framework)
# from rest_framework import viewsets, permissions
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [permissions.IsAuthenticated]
# # api/views.py
# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticated

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [permissions.IsAuthenticated] 


# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer

# # api/views.py
# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
# # api/views.py
# from rest_framework import generics
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetListCreateView(generics.ListCreateAPIView):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer

# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticated

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticated]

# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticated

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticated]

# from rest_framework import generics
# from .models import Sweet
# from .serializers import SweetSerializer

# class SweetListCreateView(generics.ListCreateAPIView):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer

# class SweetDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer

# # views.py
# from rest_framework import viewsets
# from .models import Sweet
# from .serializers import SweetSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# from rest_framework.parsers import MultiPartParser, FormParser

# class SweetViewSet(viewsets.ModelViewSet):
#     queryset = Sweet.objects.all()
#     serializer_class = SweetSerializer
#     parser_classes = (MultiPartParser, FormParser)

# # api/views.py
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Sweet, Purchase
# from .serializers import PurchaseSerializer

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_purchase(request):
#     sweet_id = request.data.get('sweet_id')
#     quantity = int(request.data.get('quantity', 1))

#     try:
#         sweet = Sweet.objects.get(id=sweet_id)
#         purchase = Purchase.objects.create(user=request.user, sweet=sweet, quantity=quantity)
#         serializer = PurchaseSerializer(purchase)
#         return Response(serializer.data, status=201)
#     except Exception as e:
#         return Response({'error': str(e)}, status=400)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_purchases(request):
#     purchases = Purchase.objects.filter(user=request.user).order_by('-purchased_at')
#     serializer = PurchaseSerializer(purchases, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def purchase_sweet(request, pk):
#     try:
#         sweet = Sweet.objects.get(pk=pk)
#         quantity = int(request.data.get('quantity', 1))

#         if quantity > sweet.quantity_in_stock:
#             return Response({'error': 'Not enough stock'}, status=400)

#         purchase = Purchase.objects.create(
#             user=request.user,
#             sweet=sweet,
#             quantity=quantity,
#             total_price=sweet.price * quantity,
#         )
#         return Response({'message': 'Purchase successful'}, status=201)

#     except Sweet.DoesNotExist:
#         return Response({'error': 'Sweet not found'}, status=404)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user_purchases(request):
#     purchases = Purchase.objects.filter(user=request.user).select_related('sweet')
#     data = [
#         {
#             'sweet_name': p.sweet.name,
#             'price': p.sweet.price,
#             'quantity': p.quantity,
#             'total_price': p.total_price,
#             'purchased_at': p.purchased_at,
#         }
#         for p in purchases
#     ]
#     return Response(data)

# # views.py
# from rest_framework import viewsets, permissions
# from .models import Purchase
# from .serializers import PurchaseSerializer

# class PurchaseViewSet(viewsets.ModelViewSet):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# # api/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import Sweet, Purchase

# class PurchaseSweetView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, sweet_id):
#         try:
#             sweet = Sweet.objects.get(id=sweet_id)
#             quantity = request.data.get("quantity", 1)

#             purchase = Purchase.objects.create(
#                 user=request.user,
#                 sweet=sweet,
#                 quantity=quantity
#             )
#             return Response({"message": "Sweet purchased successfully"}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# # views.py
# from rest_framework.generics import ListAPIView
# from .models import Purchase
# from .serializers import PurchaseSerializer
# from rest_framework.permissions import IsAuthenticated

# class PurchaseListView(ListAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

# # In views.py (protected view)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def purchase_sweet(request, sweet_id):
#     try:
#         sweet = Sweet.objects.get(id=sweet_id)
#         quantity = int(request.data.get('quantity', 1))

#         if sweet.quantity_in_stock < quantity:
#             return Response({"error": "Not enough stock."}, status=400)

#         total_price = sweet.price_per_kg * quantity

#         sweet.quantity_in_stock -= quantity
#         sweet.save()

#         purchase = Purchase.objects.create(
#             user=request.user,
#             sweet=sweet,
#             quantity=quantity,
#             total_price=total_price
#         )

#         return Response({"message": "Purchase successful."}, status=201)
#     except Sweet.DoesNotExist:
#         return Response({"error": "Sweet not found."}, status=404)

# # views.py
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Sweet, Purchase

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def purchase_sweet(request, sweet_id):
#     try:
#         sweet = Sweet.objects.get(id=sweet_id)
#         quantity = request.data.get("quantity", 1)

#         Purchase.objects.create(
#             user=request.user,
#             sweet=sweet,
#             quantity=quantity
#         )
#         return Response({"message": "Sweet added to cart successfully!"})
#     except Sweet.DoesNotExist:
#         return Response({"error": "Sweet not found."}, status=404)

# from rest_framework import generics, permissions
# from .models import Purchase
# from .serializers import PurchaseSerializer

# class PurchaseListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Purchase.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .models import Sweet, Purchase
# from .serializers import PurchaseSerializer

# class PurchaseCreateView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         sweet_id = request.data.get('sweet')
#         quantity = int(request.data.get('quantity', 0))

#         try:
#             sweet = Sweet.objects.get(id=sweet_id)
#         except Sweet.DoesNotExist:
#             return Response({"error": "Sweet not found."}, status=status.HTTP_404_NOT_FOUND)

#         if quantity <= 0:
#             return Response({"error": "Quantity must be positive."}, status=status.HTTP_400_BAD_REQUEST)

#         if sweet.stock < quantity:
#             return Response({"error": f"Only {sweet.stock} in stock."}, status=status.HTTP_400_BAD_REQUEST)

#         purchase = Purchase.objects.create(
#             user=user,
#             sweet=sweet,
#             quantity=quantity,
#             total_price=sweet.price_per_kg * quantity
#         )

#         sweet.stock -= quantity
#         sweet.save()

#         serializer = PurchaseSerializer(purchase)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

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
