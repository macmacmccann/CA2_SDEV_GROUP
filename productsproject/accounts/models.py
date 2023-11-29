from django.db import models
from django.contrib.auth.models import AbstractUser,Group
# Create your models here.



class CustomUser(AbstractUser):
    
    id = models.BigAutoField(primary_key=True)

    
    email = models.EmailField(unique=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    # auth.Group is used to organise users built in 
    # Its adds foreign key to the model pointing to auth.group to allow each user to be specified to a group 
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True,db_column='group_id')

    #'auth.Group'