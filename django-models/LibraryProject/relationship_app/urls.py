from django.urls import path
from . import views

urlpatterns = [
    path('listBooks/', views.listBooks, name='List'),
    path('libraryView', views.libraryDetailView, name='library details'),
]