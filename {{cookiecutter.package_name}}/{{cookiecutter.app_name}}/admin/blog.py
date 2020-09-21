# -*- coding: utf-8 -*-
"""
Blog admin interface
"""
from django.contrib import admin

from ..models import Blog


class BlogAdmin(admin.ModelAdmin):
    pass


# Registering interface to model
admin.site.register(Blog, BlogAdmin)
