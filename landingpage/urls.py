from django.urls import path
from landingpage import views

app_name = 'landingpage'

urlpatterns = [
    path("", views.index.as_view(), name='home'),
    path("blog", views.blog.as_view(), name='blog'),
    path("vendor", views.vender, name='vendor'),
    # path("sign-in", views.signin, name='signin'),
    path("all-vendors", views.allVendors, name='allVendors'),
    path("single-restaurant", views.singleRestaurant, name='single-restaurant'),
    path("blog-details", views.blogDetails, name='blog-details'),
]


