from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.views import LoginView
from accounts.models import User, Student, Teacher

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'gwtc@gmail.com', 'style': 'border-radius: 0px;'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'gwtc', 'style': 'border-radius: 0px;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'style': 'border-radius: 0px;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'style': 'border-radius: 0px;'}))
    # password1 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    # prepopulated_fields = {'username': ('first_name', 'last_name',)}

    class Meta():
        model = User
        fields = ('email','username','password1','password2',)
        # fields = '__all__'

# exclude = ('company',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email address already exists")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class MyLoginForm(LoginView):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'password')


    def clean_email(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(email=username)
        if qs.exists():
            raise forms.ValidationError("Email address already exists")
        return username
    



# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
# class
class StudentForm(forms.ModelForm):
    # password0 = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    # prepopulated_fields = {'username': ('first_name', 'last_name',)}

    class Meta():
        model = Student
        # fields = ('email', 'first_name', 'last_name')
        fields = '__all__'

    def save(self, commit=True):
        # Save the provided password in hashed format
        student = super(StudentForm, self).save(commit=False)
        # product.set_password(self.cleaned_data["password1"])

        if commit:
            student.save()
        return student

class TeacherForm(forms.ModelForm):
    # password0 = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    # prepopulated_fields = {'username': ('first_name', 'last_name',)}

    class Meta():
        model = Teacher
        # fields = ('email', 'first_name', 'last_name')
        fields = '__all__'

    def save(self, commit=True):
        # Save the provided password in hashed format
        teacher = super(TeacherForm, self).save(commit=False)
        # product.set_password(self.cleaned_data["password1"])

        if commit:
            teacher.save()
        return teacher

# 