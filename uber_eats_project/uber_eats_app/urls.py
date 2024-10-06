from django.urls import path
from . import views

urlpatterns = [
    path('signup/customer/', views.customer_signup, name='customer-signup'),
    path('signup/restaurant/', views.restaurant_signup, name='restaurant-signup'),
    path('profile/customer/', views.customer_profile, name='customer-profile'),
    path('profile/restaurant/', views.restaurant_profile, name='restaurant-profile'),
    path('restaurant/<int:restaurant_id>/dishes/', views.restaurant_dishes, name='restaurant-dishes'),
    path('order/', views.place_order, name='place-order'),
    path('orders/', views.customer_orders, name='customer-orders'),
]
