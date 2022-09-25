from django.contrib import admin

from landingpage.views import landingpage
from .models import Food, FoodCategories, Restaurant, RestaurantCategories, RestaurantFeatures, Team

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategories)
admin.site.register(Restaurant)
admin.site.register(RestaurantCategories)
admin.site.register(RestaurantFeatures)
admin.site.register(Team)