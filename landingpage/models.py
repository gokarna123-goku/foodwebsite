from django.db import models
import uuid
from accounts.models import User

# Create your models here.

# Food Categories
class FoodCategories(models.Model):
    food_category_image = models.ImageField(default="food.png", blank = False, upload_to = "media/food_categories_images")
    food_category_name = models.CharField(max_length=50)
    restaurant_count = models.IntegerField()

    def __str__(self):
        return self.food_category_name


# Food Items
class Food(models.Model):
    food_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food_name = models.CharField(max_length=30)
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    food_desc = models.TextField()
    food_image = models.ImageField(upload_to = 'media/food_images')

    def __str__(self):
        return self.food_name

# Order
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Menu 
class Menu(models.Model):
    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_price = models.DecimalField(max_digits=5, decimal_places=2)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)


# Order Item
class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_quantity = models.IntegerField()
    food_total_price = models.DecimalField(max_digits=5, decimal_places=2)


# Restaurant Features
class RestaurantFeatures(models.Model):
    restaurant_features_name = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_features_name


# Restaurant 
class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_name = models.CharField(max_length=60)
    restaurant_location = models.CharField(max_length=100)
    restaurant_features = models.ForeignKey(RestaurantFeatures, on_delete=models.CASCADE, null=True)
    # restaurant_features = models.Multivalue()
    restaurnat_ratings = models.CharField(max_length=10)
    restaurant_reviews = models.TextField()
    restaurant_info = models.TextField()
    restaurant_opening_closing_time = models.CharField(max_length=50)
    total_tables = models.IntegerField()
    available_tables = models.IntegerField()
    booked_tables = models.IntegerField()
    restaurant_image = models.ImageField(default= "default.png", upload_to = "media/restaurant_images")
    # food_menu = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant_name


# restaurant category
class RestaurantCategories(models.Model):
    category_name = models.CharField(max_length=50)
    restaurant_type = models.CharField(max_length=40)


# food category 
# class FoodCategories(models.Model):
#     food_category_name =  
