from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from django.urls import path
from django.views.generic import TemplateView


from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import Group


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'registration/signup.html'


    def post(self, request, *args, **kwargs): 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            signup_user = CustomUser.objects.get(username=username) 
            group = form.cleaned_data.get('group') 
            group.user_set.add(signup_user) 
            return redirect('signup_success') 
        else: 
            return render(request, self.template_name, {'form' : form }) 

