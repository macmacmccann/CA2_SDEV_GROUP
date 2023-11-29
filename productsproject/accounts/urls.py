from django.urls import path

from .views import SignUpView
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('signup_success/',TemplateView.as_view(template_name='registration/signup_success.html'),name = 'signup_success'),
]