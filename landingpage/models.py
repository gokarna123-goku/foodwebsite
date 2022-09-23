from django.db import models
import uuid

# Create your models here.

# Food Categories
class FoodCategories(models.Model):
    food_type = models.CharField(max_length=30)
    food_category = models.CharField(max_length=10)


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



# Restaurant 
class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_name = models.CharField(max_length=60)
    restaurant_location = models.CharField(max_length=100)
    restaurant_features = models.CharField(max_length=120)
    restaurnat_ratings = models.CharField(max_length=10)
    restaurant_reviews = models.TextField()
    restaurant_info = models.TextField()
    restaurant_opening_closing_time = models.CharField(max_length=50)
    restaurant_image = models.ImageField(default= "default.png",upload_to = "media/restaurant_images")
    food_menu = models.ForeignKey(Food, on_delete=models.CASCADE)


# restaurant category
class RestaurantCategories(models.Model):
    category_name = models.CharField(max_length=50)
    restaurant_type = models.CharField(max_length=40)


# food category 
# class FoodCategories(models.Model):
#     food_category_name =  
