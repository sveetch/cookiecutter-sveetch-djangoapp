"""
CMS Plugins installations
"""
from cms.plugin_pool import plugin_pool

from .plugins.blog import BlogPlugin


plugin_pool.register_plugin(BlogPlugin)
