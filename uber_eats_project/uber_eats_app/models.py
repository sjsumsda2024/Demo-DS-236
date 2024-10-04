from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)

    # Adding related_name to avoid clashes with the default auth.User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='uber_eats_app_users',  # Customize related_name here
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='uber_eats_app_users_permissions',  # Customize related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    favorite_restaurants = models.ManyToManyField('Restaurant', blank=True)

    def __str__(self):
        return self.user.username
    
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)  # e.g., 'Appetizer', 'Main Course'

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('preparing', 'Preparing'),
        ('on_the_way', 'On the Way'),
        ('delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.user.username}"

# Create your models here.
