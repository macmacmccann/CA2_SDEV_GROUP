from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group

# Register your models here.
class CustomUserCreationForm(UserCreationForm):

    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('username','email','age','iq_level' , 'coding_level','address', 'group')

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+( 'username','email','age','iq_level' , 'coding_level','address', 'group')
  