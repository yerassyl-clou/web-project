from rest_framework import serializers
from .models import Manufacturer, Plane, Order, Customer

# Manufacturer Serializer
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'description', 'headquarters_city', 'headquarters_address']

# Plane Serializer
class PlaneSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Plane
        fields = ['id', 'name', 'description', 'price', 'manufacturer']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    plane = serializers.PrimaryKeyRelatedField(queryset=Plane.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'customer', 'plane', 'order_date', 'status']

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone_number', 'address']

# Plane Search Serializer (for filtering by keyword)
class PlaneSearchSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=100)
