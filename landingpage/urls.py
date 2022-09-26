from django.urls import path
from landingpage import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'landingpage'

urlpatterns = [
    path("", views.index.as_view(), name='home'),
    path("blog", views.blog.as_view(), name='blog'),
    path("vendor", views.vender, name='vendor'),
    # path("sign-in", views.signin, name='signin'),
    path("all-vendors", views.allVendors, name='allVendors'),
    path("single-restaurant", views.singleRestaurant, name='single-restaurant'),
    path("blog-details", views.blogDetails, name='blog-details'),
    path('restaurant_detail/<str:restaurant_id>/', views.RestaurantDetails.as_view(), name='restaurant_detail')
]


urlpatterns += [
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# 