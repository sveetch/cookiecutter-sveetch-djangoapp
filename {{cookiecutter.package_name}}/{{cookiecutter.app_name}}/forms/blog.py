from django import forms

from ..models.blog import BlogPluginModel


class BlogPluginForm(forms.ModelForm):
    class Meta:
        model = BlogPluginModel
        exclude = []
        fields = [
            "blog",
            "limit",
        ]
