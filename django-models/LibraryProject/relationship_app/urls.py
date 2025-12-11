from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('listBooks/', views.list_books, name='List'),
    path('libraryView/', views.LibraryDetailView, name='library details'),
]