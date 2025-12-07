from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("register")
    template_name = "templates/blog/registration/register.html"
# Create your views here.
