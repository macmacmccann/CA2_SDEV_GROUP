from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




    def post(self, request, *args, **kwargs): 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            signup_user = CustomUser.objects.get(username=username) 
            customer_group = form.cleaned_data.get('group') 
            customer_group.user_set.add(signup_user) 
            return redirect('login') 
        else: 
            return render(request, self.template_name, {'form' : form }) 

