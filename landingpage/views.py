from django.shortcuts import render
from django.views import generic
from landingpage.models import Blog, Food, FoodCategories, Restaurant, Team


# Create your views here.

class index(generic.ListView):
    template_name = 'landingpage/index.html'
    # model = Food
    # context_object_name = 'foods'

    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        food_categories = FoodCategories.objects.all()
        restaurants = Restaurant.objects.all()
        team = Team.objects.all()
        blogs = Blog.objects.all()
        context = {
            'foods': foods,
            'food_categories': food_categories,
            'restaurants': restaurants,
            'team': team,
            'blogs': blogs,
        }
        return render(request, self.template_name, context)


class blog(generic.ListView):
    template_name = 'landingpage/blog.html'
    model = Blog
    context_object_name = 'blogs'


class RestaurantDetails(generic.DetailView):
    def get(self, request, *args, **kwargs):
        restaurant_details = Restaurant.objects.get(restaurant_id=self.kwargs.get('restaurant_id'))
        context = {
            'restaurant_details': restaurant_details,
        }
        # print("somethinf id is: " + self.kwargs.get('restaurant_id'))
        return render(request, 'landingpage/restaurant_details.html', context)


    # model = Restaurant
    # template_name = 'landingpage/restaurant_details.html'
    # context_object_name = 'restaurant_details'



# class index(generic.ListView):
#     template_name = 'landingpage/index.html'
#     model = FoodCategories
#     context_object_name = 'food_categories'


def vender(request):
    return render(request, 'landingpage/vendor.html')


def allVendors(request):
    return render(request, 'landingpage/all-vendor.html')


def singleRestaurant(request):
    return render(request, 'landingpage/single-restaurant.html')


def blogDetails(request):
    return render(request, 'landingpage/blog_details.html')


# 