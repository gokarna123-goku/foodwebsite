from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm #CustomUserCreationForm, CustomUserChangeForm
from .models import User, Student, Teacher, Teacher_Course_Assignment, Gradecourse, Principal_Admin, Director


class UserAdmin(UserAdmin):
    add_form = RegisterForm
    # form = UserChangeForm
    model = User
    list_display = ('username','email', 'is_staff', 'is_active',)
    list_filter = ('username','email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Teacher_Course_Assignment)
admin.site.register(Gradecourse)
admin.site.register(Principal_Admin)
admin.site.register(Director)
