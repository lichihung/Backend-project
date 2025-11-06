#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, Booking
from decimal import Decimal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "stock", "price_after_tax"]

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'