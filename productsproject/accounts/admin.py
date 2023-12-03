from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile




class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


    list_display = ['username','email','age','iq_level' , 'coding_level','address', 'group']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age","group")}),)
    add_fieldsets = UserAdmin.add_fieldsets +  ((None, {"fields": ("age",)}),)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)