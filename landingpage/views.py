from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, HttpResponse

# Create your views here.
def landingpage(request):
    return render(request, 'landingpage/index.html')
    # return HttpResponse("This is HomePage")

def vender(request):
    return render(request, 'landingpage/vendor.html')


# def signin(request):
#     return render(request, 'landingpage/signin.html')


def blog(request):
    return render(request, 'landingpage/blog.html')

def allVendors(request):
    return render(request, 'landingpage/all-vendor.html')


def singleRestaurant(request):
    return render(request, 'landingpage/single-restaurant.html')


# 