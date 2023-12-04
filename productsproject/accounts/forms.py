from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile
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
  
class ProfileCreationForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['username', 'age', 'bio', 'email', 'shipping_address', 'fav_course', 'available_status', 'profile_pic']