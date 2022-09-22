from django.shortcuts import render
from django.views.generic import TemplateView, View
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# User = get_user_model()

# from accounts.tokens import account_activation_token

# Create your views here.
class HomeView(TemplateView):
    template_name = 'registration/home.html'


class UserLoginView(LoginView):
    # form_class = UserCreationForm
    # template_name = 'registration/login.html'
    template_name = 'landingpage/signin.html'
    # success_url = reverse_lazy('landingpage:home')


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('landingpage:home')
    template_name = 'registration/logged_out'
    

class RegisterView(CreateView):
    form_class = RegisterForm
    # template_name = 'registration/signup.html'
    template_name = 'landingpage/signup.html'

    def get(self, request, *args, **kwargs):
        print("get initiated")
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("form has been posted")
        if form.is_valid():
            print("form is valid")
            user = form.save(commit=False)
            #set user to inactive until the email confirmation is sent
            # user = request.user
            user.is_active = True
            user.save()
            # #send confirmation email
            # current_site = get_current_site(request)
            # subject = 'Activate your account'
            # message = render_to_string('registration/account_activate_email.html', {
            #     'user':user,
            #     'domain':current_site.domain,
            #     # 'uid':urlsafe_base64_encode(force_bytes(user.id)).decode(),
            #     'uid':urlsafe_base64_encode(force_bytes(user.id)),
            #     'token':default_token_generator.make_token(user),
            # })
            # user.email_user(subject, message, from_email=None, **kwargs)
            # messages.success(request, 'Please confirm your email to complete registration')
            # return redirect('accounts:sent')
            return redirect('landingpage:signin')
        return render(request, self.template_name, {'form':form})

class ActivateAccount(View):

     def get(self, request, uidb64, token, *args, **kwargs):
         try:
             # uid = force_bytes(urlsafe_base64_decode(uidb64)).decode()
             uid = force_bytes(urlsafe_base64_decode(uidb64))
             user = User.objects.get(id=uid)
             # print(uid)
         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            #  user = None
         # User = get_user_model()
         # print(uid)
         # uid = force_text(urlsafe_base64_decode(uidb64))#.decode()
         # # uid = int(uida,10) invalid literal for int() with base 10: b'l\xc4'
         # #the value of uid is b'l\xcc' need to convert this to 1
         # user = User.objects.get(id=uid)
         # # print(uid)

            if user is not None or default_token_generator.check_token(user, token):
                # obj, created = User.objects.get_or_create(user=user)
                user.is_active = True
                user.email_confirmed = True
                user.save()
                login(request, user)
                messages.success(request,('Your account have been confirmed.'))
                return redirect('accounts:profile')
            else:
                # messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
                # return redirect('accounts:activation_invalid')
                return HttpResponse ('The confirmation link was invalid, possibly because it has already been used.')

def activation_sent_view(request):
    return render(request,'registration/activation_sent.html')

def activation_invalid_view(request):
    return render(request,'registration/activation_invalid.html')

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')
# class StudentView(CreateView):
#     form_class = RegisterForm
#     template_name = 'registration/student_form.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form':form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             #set user to inactive until the email confirmation is sent
#             # user = request.user
#             user.is_active = False
#             user.save()
#             #send confirmation email
#             current_site = get_current_site(request)
#             subject = 'Activate your account'
#             message = render_to_string('registration/account_activate_email.html', {
#                 'user':user,
#                 'domain':current_site.domain,
#                 # 'uid':urlsafe_base64_encode(force_bytes(user.id)).decode(),
#                 'uid':urlsafe_base64_encode(force_bytes(user.id)),
#                 'token':default_token_generator.make_token(user),
#             })
#             user.email_user(subject, message, from_email=None, **kwargs)
#             messages.success(request, 'Please confirm your email to complete registration')
#             return redirect('accounts:sent')
#         return render(request, self.template_name, {'form':form})
#
# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = 'registration/signup.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form':form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             #set user to inactive until the email confirmation is sent
#             # user = request.user
#             user.is_active = False
#             user.save()
#             #send confirmation email
#             current_site = get_current_site(request)
#             subject = 'Activate your account'
#             message = render_to_string('registration/account_activate_email.html', {
#                 'user':user,
#                 'domain':current_site.domain,
#                 # 'uid':urlsafe_base64_encode(force_bytes(user.id)).decode(),
#                 'uid':urlsafe_base64_encode(force_bytes(user.id)),
#                 'token':default_token_generator.make_token(user),
#             })
#             user.email_user(subject, message, from_email=None, **kwargs)
#             messages.success(request, 'Please confirm your email to complete registration')
#             return redirect('accounts:sent')
#         return render(request, self.template_name, {'form':form})
