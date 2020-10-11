from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from ..models import Blog


class BlogIndexView(ListView):
    """
    List of blogs
    """
    model = Blog
    queryset = Blog.objects.order_by('title')
    template_name = "{{ cookiecutter.app_name }}/blog_index.html"
    paginate_by = settings.BLOG_PAGINATION


class BlogDetailView(SingleObjectMixin, ListView):
    """
    Blog detail and its related article list
    """
    pk_url_kwarg = "blog_pk"
    template_name = "{{ cookiecutter.app_name }}/blog_detail.html"
    paginate_by = settings.ARTICLE_PAGINATION
    context_object_name = "blog_object"

    def get_queryset(self):
        return self.object.article_set.order_by('title')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Blog.objects.all())

        return super().get(request, *args, **kwargs)
