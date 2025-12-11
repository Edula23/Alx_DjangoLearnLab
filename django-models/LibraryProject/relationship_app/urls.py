from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, Register
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('listBooks/', views.list_books, name='List'),
    path('libraryView/', LibraryDetailView.as_view(), name='library-details'),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.Register, name='register'),
]
"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="