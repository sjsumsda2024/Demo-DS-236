from rest_framework import serializers
from .models import Customer, Restaurant, Dish, Order, User

# Serializer for the custom User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_customer', 'is_restaurant']

# Serializer for Customer
class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ['user', 'favorite_restaurants']

# Serializer for Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Restaurant
        fields = ['user', 'name', 'location', 'description', 'contact_info']

# Serializer for Dish
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'ingredients', 'price', 'category', 'restaurant']

# Serializer for Order
class OrderSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    restaurant = RestaurantSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'dishes', 'status', 'created_at']
