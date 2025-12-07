from django.urls import path
from django.views.generic import TemplateView

from blog.views import (
    Register,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    user_profile_view,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("login/", TemplateView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("profile/", user_profile_view, name="profile"),
    path("post/<int:pk>/comments/new/", user_profile_view, name="profile"),
    path("comment/<int:pk>/delete/", user_profile_view, name="profile"),
    path("comment/<int:pk>/update/"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view()),
]

