
from django.urls import path 
from .views import HomePageView ,AboutPageView, SearchResultsListView
from . import views

app_name = 'shop'

urlpatterns = [
    
   # path('', HomePageView.as_view(), name='home'),
  #  path('about/', AboutPageView.as_view(), name='about'),

    path('', views.prod_list, name = 'all_products'),
    path('<uuid:category_id>/', views.prod_list , name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),
    path('search/',SearchResultsListView.as_view(), name = 'search_results'),

]
