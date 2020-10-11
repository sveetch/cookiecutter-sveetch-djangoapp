"""
Application URLs
"""
from django.urls import path

from {{ cookiecutter.app_name }}.views import (
    BlogIndexView, BlogDetailView,
    ArticleDetailView,
)


app_name = "{{ cookiecutter.app_name }}"


urlpatterns = [
    path("", BlogIndexView.as_view(), name="blog-index"),
    path("<int:blog_pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path(
        "<int:blog_pk>/<int:article_pk>/",
        ArticleDetailView.as_view(),
        name="article-detail"
    ),
]
