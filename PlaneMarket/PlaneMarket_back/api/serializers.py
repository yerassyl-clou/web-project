from rest_framework import serializers
from .models import Manufacturer, Plane, Order, Customer

# Manufacturer Serializer
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'description', 'headquarters_city', 'headquarters_address']

# Plane Serializer
class PlaneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    image_url = serializers.URLField(required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Plane.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance


# Order Serializer
class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    plane = serializers.PrimaryKeyRelatedField(queryset=Plane.objects.all())
    order_date = serializers.DateField()
    status = serializers.CharField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone_number', 'address']

# Plane Search Serializer (for filtering by keyword)
class PlaneSearchSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=100)
