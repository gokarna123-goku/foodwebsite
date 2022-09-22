
from django.contrib import admin
from django.urls import path
from landingpage import views

app_name = 'landingpage'

urlpatterns = [
    path("", views.landingpage, name='home'),
    path("vendor", views.vender, name='vendor'),
    # path("sign-in", views.signin, name='signin'),
    path("blog", views.blog, name='blog'),
    path("all-vendors", views.allVendors, name='allVendors'),
    path("single-restaurant", views.singleRestaurant, name='single-restaurant'),
]
