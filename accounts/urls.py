from django.urls import path
from accounts import views
from django.views.generic.base import TemplateView
# from .views import profile

app_name = 'accounts'

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='registration/home.html'), name='home'),
    # path('signup/', views.RegisterView.as_view(template_name='registration/signup.html'), name='signup'),
    path('signup/', views.RegisterView.as_view(template_name='landingpage/signin.html'), name='signup'),
    path('signin/', views.UserLoginView.as_view(template_name='landingpage/signin.html'), name='signin'),
    path('logged_out/', views.UserLogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('activate/<str:uidb64>/<str:token>', views.ActivateAccount.as_view(),name='activate'),
    path('sent/', views.activation_sent_view, name='sent'),
    path('invalid',views.activation_invalid_view, name='invalid'),
    # path('profile/', profile, name='users-profile'),
]
