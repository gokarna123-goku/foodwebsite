from django.contrib import admin
from .models import Blog, Food, FoodCategories, Restaurant, RestaurantCategories, RestaurantFeatures, Team

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategories)
admin.site.register(Restaurant)
admin.site.register(RestaurantCategories)
admin.site.register(RestaurantFeatures)
admin.site.register(Team)
admin.site.register(Blog)