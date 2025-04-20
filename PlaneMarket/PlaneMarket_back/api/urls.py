from django.urls import path

from .views import (
    manufacturers_list,
    manufacturer_detail,
    planes_by_manufacturer,
    PlaneListAPIView,
    PlaneDetailAPIView,
    TopTenPlaneListAPIView,
    orders_by_plane,
    customer_orders,
    create_order_for_authenticated_user,
    
)

urlpatterns = [
    path('manuafacturers/', manufacturers_list),
    path('manuafacturers/<int:id>/', manufacturer_detail),
    path('manuafacturers/<int:id>/planes/', planes_by_manufacturer),

    path('planes/', PlaneListAPIView.as_view()),
    path('planes/<int:id>/', PlaneDetailAPIView.as_view()),
    path('planes/top_ten/', TopTenPlaneListAPIView.as_view()),
    path('planes/<int:id>/orders/', orders_by_plane),

    path('customers/<int:id>/orders', customer_orders),
    path('orders/create/', create_order_for_authenticated_user),

    #path('orders/<int:id>/', OrderDetailAPIView.as_view()),

    #path('login/'),                                             #TO_DO
    #path('logout/')                                             #TO_DO
]