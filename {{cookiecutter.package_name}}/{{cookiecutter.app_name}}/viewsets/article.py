"""
=================
Article API views
=================

"""
from rest_framework import viewsets

from ..models import Article
from ..serializers import ArticleSerializer, ArticleResumeSerializer

from .mixins import ConditionalResumedSerializerMixin


class ArticleViewSet(ConditionalResumedSerializerMixin, viewsets.ModelViewSet):
    """
    Viewset for all HTTP methods on Article model.
    """
    model = Article
    serializer_class = ArticleSerializer
    resumed_serializer_class = ArticleResumeSerializer

    def get_queryset(self):
        return self.model.objects.all()
