# -*- coding: utf-8 -*-
import factory

from ..models import Article

from .blog import BlogFactory


class ArticleFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of an Article.
    """
    blog = factory.SubFactory(BlogFactory)
    title = factory.Faker("text", max_nb_chars=50)
    content = factory.Faker("text", max_nb_chars=150)

    class Meta:
        model = Article
