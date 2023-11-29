from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group

# Register your models here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('username','email','age',)
        group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = UserCreationForm.Meta.fields+('username','email','age',)

