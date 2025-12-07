from django.urls import path, include
from django.views.generic import TemplateView 
from blog.views import SignUpView
urlpatterns = [
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='accounts/register.html'), name='register'),
    path("profile/", SignUpView.as_view(), name="templates/registration/profile."),
]
