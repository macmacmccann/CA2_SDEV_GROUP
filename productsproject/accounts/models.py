from django.db import models
from django.contrib.auth.models import AbstractUser,Group


#Imports for profile class 
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=False)
    age = models.PositiveIntegerField(null=True, blank=True,default=0)

    iq_level = models.PositiveIntegerField(null=True, blank=True,default = 0)
    coding_level = models.PositiveIntegerField(null=True, blank=True,default = 0)
    address = models.CharField(max_length=100 ,default = 0 )
    image = models.ImageField(upload_to='users', null=True, blank=True)

    # auth.Group is used to organise users built in 
    # Its adds foreign key to the model pointing to auth.group to allow each user to be specified to a group 
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True,db_column='group_id')

    #'auth.Group'

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
 
    bio = models.TextField(blank=True)
    # Referencing user model 
    profile_pic = models.ImageField(upload_to='users', null=True, blank=True)

    available_status = models.BooleanField(default=False)
    # Using a foreig key to connect to the model product and get all produts 
    fav_course = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return str (self.user)

    def get_absolute_url(self):
        return reverse('show_profile',args = [str(self.id)])