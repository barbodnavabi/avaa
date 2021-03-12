from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from Business.models import Agents
from Blog.models import Article


class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 1

    def items(self):
        return Article.objects.published()

    def lastmod(self, obj):
        return obj.publish


class AgentSitemap(Sitemap):
    changefreq = "always"
    priority = 1

    def items(self):
        return Agents.objects.all()

    def lastmod(self, obj):
        return obj.timeadd


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    def items(self):
        return ['contact', 'index','agents']

    def location(self, item):
        return reverse(item)
