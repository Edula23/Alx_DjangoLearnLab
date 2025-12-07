from django.urls import path, include
from django.views.generic import TemplateView 
from blog.views import Register
urlpatterns = [
    path('login/', TemplateView.as_view(template_name='templates/blog/registration/login.html'), name='login'), 
    path("profile/", TemplateView.as_view(), template_name="templates/accounts/profile.html", name='profile' ),
    path('register/', Register.as_view(template_name='templates/blog/registration/register.html'), name='register'), ]
   