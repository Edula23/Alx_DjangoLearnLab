from django.urls import path
from . import views
from .views import list_books, libraryDetailView
urlpatterns = [
    path('listBooks/', views.list_books, name='List'),
    path('libraryView', views.libraryDetailView, name='library details'),
]