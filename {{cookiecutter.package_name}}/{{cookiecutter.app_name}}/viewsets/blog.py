"""
==============
Blog API views
==============

"""
from rest_framework import viewsets

from ..models import Blog
from ..serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    Viewset for all HTTP methods on Blog model.
    """
    model = Blog
    serializer_class = BlogSerializer

    def get_queryset(self):
        return self.model.objects.all()
