# from django.contrib.auth.models import User
# from rest_framework import serializers
# from .models import Sweet

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user




# class SweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sweet
#         fields = '__all__'

# # serializers.py
# from rest_framework import serializers
# from .models import Sweet

# class SweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sweet
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Sweet

# class SweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sweet
#         fields = '__all__'


# from rest_framework import serializers
# from .models import Sweet

# class SweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sweet
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Purchase

# class PurchaseSerializer(serializers.ModelSerializer):
#     sweet_name = serializers.CharField(source='sweet.name', read_only=True)

#     class Meta:
#         model = Purchase
#         fields = ['id', 'sweet_name', 'quantity', 'total_price', 'purchased_at']

# # serializers.py
# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = '__all__'
#         read_only_fields = ['user', 'total_price', 'purchased_at']

# from rest_framework import serializers
# from .models import Purchase

# class PurchaseSerializer(serializers.ModelSerializer):
#     sweet_name = serializers.CharField(source='sweet.name', read_only=True)

#     class Meta:
#         model = Purchase
#         fields = ['id', 'sweet', 'sweet_name', 'quantity', 'total_price', 'purchased_at']
#         read_only_fields = ['total_price', 'purchased_at']

# from rest_framework import serializers
# from .models import Purchase

# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         fields = ['id', 'user', 'sweet', 'quantity', 'total_price', 'purchased_at']
#         read_only_fields = ['total_price', 'user', 'purchased_at']

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Sweet, Purchase


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# Sweet Serializer
class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = '__all__'


# Purchase Serializer (basic)
class PurchaseSerializer(serializers.ModelSerializer):
    sweet_name = serializers.CharField(source='sweet.name', read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'sweet', 'sweet_name', 'quantity', 'total_price', 'purchased_at']
        read_only_fields = ['user', 'total_price', 'purchased_at']
