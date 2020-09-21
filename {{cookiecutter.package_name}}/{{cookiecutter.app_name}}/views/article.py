from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView


from ..models import Blog, Article


class ArticleDetailView(DetailView):
    """
    Article detail
    """
    pk_url_kwarg = "article_pk"
    template_name = "{{ cookiecutter.app_name }}/article_detail.html"

    def get_queryset(self):
        """
        Get article object, we validate it is related to required blog from
        query argument and set the blog object as an attribute for template
        context.
        """
        self.blog_object = get_object_or_404(
            Blog,
            pk=self.kwargs.get("blog_pk"),
        )

        return Article.objects.filter(blog=blog_object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_object"] = self.blog_object

        return context
