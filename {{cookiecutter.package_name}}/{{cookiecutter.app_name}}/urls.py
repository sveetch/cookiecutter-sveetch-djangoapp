from django.urls import path{% if cookiecutter.include_api|lower == 'true' %}, include{% endif %}

from .views import (
    BlogIndexView, BlogDetailView,
    ArticleDetailView,
){% if cookiecutter.include_api|lower == 'true' %}
from .routers import router{% endif %}


app_name = "{{ cookiecutter.app_name }}"


urlpatterns = [
    path("", BlogIndexView.as_view(), name="blog-index"),{% if cookiecutter.include_api|lower == 'true' %}
    path("api/", include(router.urls)),{% endif %}
    path("<int:blog_pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path(
        "<int:blog_pk>/<int:article_pk>/",
        ArticleDetailView.as_view(),
        name="article-detail"
    ),
]
