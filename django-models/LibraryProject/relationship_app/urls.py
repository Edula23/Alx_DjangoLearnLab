from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, Register
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('listBooks/', views.list_books, name='List'),
    path('libraryView/<int:pk>/', LibraryDetailView.as_view(), name='library-details'),
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
    path('register/', Register.as_view(template_name = 'relationship_app/register.html'), name='register'),
]
"views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="