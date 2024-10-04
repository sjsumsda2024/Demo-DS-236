from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Customer, Restaurant, Dish, Order
from .serializers import CustomerSerializer, RestaurantSerializer, DishSerializer, OrderSerializer

# Customer signup
@api_view(['POST'])
def customer_signup(request):
    if request.method == 'POST':
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            is_customer=True
        )
        customer = Customer.objects.create(user=user)
        return Response({'message': 'Customer created successfully'}, status=status.HTTP_201_CREATED)

# Restaurant signup
@api_view(['POST'])
def restaurant_signup(request):
    if request.method == 'POST':
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            is_restaurant=True
        )
        restaurant = Restaurant.objects.create(user=user, name=data['name'], location=data['location'])
        return Response({'message': 'Restaurant created successfully'}, status=status.HTTP_201_CREATED)

# Get Customer profile
@api_view(['GET'])
def customer_profile(request):
    try:
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

# Get Restaurant profile
@api_view(['GET'])
def restaurant_profile(request):
    try:
        restaurant = request.user.restaurant
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

# Get list of dishes for a restaurant
@api_view(['GET'])
def restaurant_dishes(request, restaurant_id):
    try:
        dishes = Dish.objects.filter(restaurant_id=restaurant_id)
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response({'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

# Order management
@api_view(['POST'])
def place_order(request):
    customer = request.user.customer
    restaurant_id = request.data['restaurant']
    dishes = request.data['dishes']

    restaurant = Restaurant.objects.get(id=restaurant_id)
    order = Order.objects.create(customer=customer, restaurant=restaurant)

    for dish_id in dishes:
        dish = Dish.objects.get(id=dish_id)
        order.dishes.add(dish)

    order.save()
    return Response({'message': 'Order placed successfully'}, status=status.HTTP_201_CREATED)

# List of customer orders
@api_view(['GET'])
def customer_orders(request):
    orders = Order.objects.filter(customer=request.user.customer)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
