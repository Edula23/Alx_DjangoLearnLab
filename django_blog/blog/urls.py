from django.urls import path
from django.views.generic import TemplateView

from blog.views import (
    Register,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    user_profile_view,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("login/", TemplateView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("profile/", user_profile_view, name="profile"),
]
   