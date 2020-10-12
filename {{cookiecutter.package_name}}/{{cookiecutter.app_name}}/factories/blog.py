# -*- coding: utf-8 -*-
import factory

from ..models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of a Blog.
    """
    title = factory.Faker("text", max_nb_chars=50)

    class Meta:
        model = Blog
