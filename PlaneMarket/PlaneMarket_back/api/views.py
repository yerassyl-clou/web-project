from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Manufacturer, Plane, Customer, Order
from .serializers import ManufacturerSerializer, PlaneSerializer, OrderSerializer, CustomerSerializer


@api_view(['GET', 'POST'])
def manufacturers_list(request):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def manufacturer_detail(request, id):
    manufacturer = Manufacturer.objects.get(id=id)

    if request.method == 'GET':
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def planes_by_manufacturer(request, id):
    planes = Plane.objects.filter(manufacturer_id=id)
    if not planes:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PlaneSerializer(planes, many=True)
    return Response(serializer.data)



class PlaneListAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        planes = Plane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaneDetailAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            plane = get_object_or_404(Plane, id=id)
        except Plane.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneSerializer(plane)
        return Response(serializer.data)

    def put(self, request, id):
        plane = Plane.objects.get(id=id)
        serializer = PlaneSerializer(plane, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        plane = Plane.objects.get(id=id)
        plane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TopTenPlaneListAPIView(APIView):
    def get(self, request):
        planes = Plane.objects.order_by('-price')[:10]
        if not planes:
            return Response({"detail": "No planes found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneSerializer(planes, many=True)
        return Response(serializer.data)


class PlaneViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()

    def perform_create(self, serializer):
        serializer.save(manufacturer=self.request.user.manufacturer)


@api_view(['GET'])
def orders_by_plane(request, id):
    orders = Order.objects.filter(plane_id=id)
    if not orders:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customer_orders(request, id):
    orders = Order.objects.filter(customer_id=id)
    if not orders:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_order_for_authenticated_user(request):
    customer = getattr(request.user, 'customer', None)
    if not customer:
        return Response({"detail": "Authenticated user has no linked customer profile."}, status=status.HTTP_400_BAD_REQUEST)

    plane_id = request.data.get('plane')
    if not plane_id:
        return Response({"detail": "Plane ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        plane = Plane.objects.get(id=plane_id)
    except Plane.DoesNotExist:
        return Response({"detail": "Plane not found."}, status=status.HTTP_404_NOT_FOUND)

    order = Order.objects.create(customer=customer, plane=plane, status="pending")
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

#TODO
#Надо сделать одну функцию def create_order_for_authenticated_user + login/logout jwt

#class MyTokenObtainPairView(TokenObtainPairView):

# @api_view(['POST'])
# def create_order_for_authenticated_user(request):

# @api_view(['POST'])
# def logout_view(request):