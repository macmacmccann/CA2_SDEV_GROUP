from django.urls import path
from .views import search_users


app_name = 'search'
urlpatterns = [
    path('search_users/', search_users, name='search_users'),
]