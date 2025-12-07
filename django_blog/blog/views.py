from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("register")
    template_name = "templates/blog/registration/register.html"




@login_required
def user_profile_view(request):
    # Get the current user
    user = request.user
    
    # If the request is a POST request, process the form data
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        
        # If the form is valid, save the changes and redirect to the profile page
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile_view')
        else:
            messages.error(request, "Error updating profile. Please try again.")
    
    # If the request is a GET request, create a form instance for the user
    else:
        form = UserProfileForm(instance=user)
    
    # Render the profile page with the form
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'user_profile.html', context)

# Create your views here.
