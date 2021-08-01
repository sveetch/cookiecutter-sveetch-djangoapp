"""
Application API URLs
"""
from rest_framework import routers

from .viewsets import ArticleViewSet, BlogViewSet


# API router
router = routers.DefaultRouter()

router.register(
    r"blogs",
    BlogViewSet,
    basename="api-blog"
)

router.register(
    r"articles",
    ArticleViewSet,
    basename="api-article"
)
