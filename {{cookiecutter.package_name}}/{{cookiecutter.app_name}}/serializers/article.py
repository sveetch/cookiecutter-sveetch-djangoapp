from rest_framework import serializers

from ..models import Article
from .blog import BlogIdField, BlogResumeSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Complete representation for detail and writing usage.

    Blog relation have two serializer fields, one for read only to return resumed
    details and another one for write only with complete detail and which expect a
    blog ID.
    """
    id = serializers.ReadOnlyField()
    view_url = serializers.SerializerMethodField()
    blog = BlogResumeSerializer(read_only=True)
    blog_id = BlogIdField(write_only=True, source='blog')

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            "url": {
                "view_name": "{{ cookiecutter.app_name }}:api-article-detail"
            },
            # DRF does not consider fields with ``blank=True`` and ``default=""`` as
            # required
            "title": {
                "required": True
            },
        }

    def get_view_url(self, obj):
        """
        Return the HTML detail view URL.

        If request has been given to serializer this will be an absolute URL, else a
        relative URL.
        """
        url = obj.get_absolute_url()
        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(url)

        return url


class ArticleResumeSerializer(ArticleSerializer):
    """
    Simpler Article representation for nested list. It won't be suitable for writing
    usage.
    """
    class Meta:
        model = ArticleSerializer.Meta.model
        fields = ["id", "url", "view_url", "blog", "publish_start", "title"]
        extra_kwargs = ArticleSerializer.Meta.extra_kwargs
