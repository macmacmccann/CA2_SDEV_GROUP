from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from django.urls import path
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.contrib.auth import get_user_model


from accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import Group

from .models import Profile


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
            return redirect('create_profile') 
        else: 
            return render(request, self.template_name, {'form' : form }) 


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['fav_course', 'bio', 'available_status','profile_pic']

class ProfileEditStatusView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_status.html'
    fields = [ 'available_status']
    context_object_name = 'current_profile'
   # pk = self.kwargs.get('pk')
    #profile = get_object_or_404(Profile, pk=pk) 


    def get_object(self):
        # Retrieve the object based on the captured primary key
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk=pk)

    def update_avail(self,request):
        user = request.user  


        # Toggle the availability status
        if user.profile.available_status == True:
            user.profile.available_status = False
        elif user.profile.available_status == False:
            user.profile.available_status = True

        user.profile.save()

        return redirect('user_profile')

        #return render(request, 'registration/edit_profile_status.html', {'current_profile': self.object })




class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'


class ProfileCreationView(View):
    template_name = 'registration/create_profile.html'

    def get(self, request, *args, **kwargs):
        form = ProfileCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)


  # Ensure request.user is a CustomUser instance
            if isinstance(request.user, get_user_model()):
                profile.user = request.user
                profile.save()
                return redirect('view_profile')
            else:
                # Handle the case when request.user is not a CustomUser instance
                # This could happen if the user is not authenticated
                return render(request, 'base.html', {'error_message': 'Invalid user type'})


      
        return render(request, self.template_name, {'form': form})

