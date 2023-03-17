from rest_framework import serializers

from ..models import Blog


class BlogIdField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Blog.objects.all()


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    """
    Complete representation for detail and writing usage.
    """
    id = serializers.ReadOnlyField()
    view_url = serializers.SerializerMethodField()
    article_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            "url": {
                "view_name": "{{ cookiecutter.app_name }}:api-blog-detail"
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

    def get_article_count(self, obj):
        """
        Return count of related articles.
        """
        return obj.article_set.count()


class BlogResumeSerializer(BlogSerializer):
    """
    Simpler Blog representation for nested list. It won't be suitable for writing
    usage.
    """
    class Meta:
        model = BlogSerializer.Meta.model
        fields = ["id", "url", "view_url", "title"]
        extra_kwargs = BlogSerializer.Meta.extra_kwargs
