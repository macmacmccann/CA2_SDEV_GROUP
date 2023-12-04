from django.urls import path

from .views import SignUpView, ProfileEditView, ProfilePageView,ProfileEditStatusView,ProfileCreationView
from . import views
from django.views.generic import TemplateView




urlpatterns = [

    path('signup/', SignUpView.as_view(), name = 'signup'),

    path('signup_success/',TemplateView.as_view(template_name='registration/signup_success.html'),name = 'signup_success'),
    path('edit_profile/<int:pk>/', ProfileEditView.as_view(),name= 'edit_profile'),
    path('edit_profile_status/<int:pk>/', ProfileEditStatusView.as_view(), name='edit_profile_status'),

    path('create_profile/', ProfileCreationView.as_view(), name='create_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(),name= 'show_profile'),
    path('update_avail/<int:pk>/', ProfileEditStatusView.as_view(), name='update_avail'),




]