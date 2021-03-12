from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemap import StaticViewSitemap, BlogSitemap,AgentSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog':BlogSitemap,
    'AgentSitemap':AgentSitemap,

}
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]