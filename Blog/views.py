from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article,Tags
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Article, Tags
from django.http import request, Http404
from django.views.generic import DetailView, ListView
from django.contrib.sitemaps import Sitemap


class BlogListView(ListView):
    queryset= Article.objects.filter(status='p')
    model = Article
    paginate_by = 9
    template_name = "blog/blog_list.html"


    
class ArticleDetail(DetailView):
    template_name = 'blog/Article-detail.html'

    def get_object(self):
        global article
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(status='p').order_by("-publish")
        context['tags'] = Tags.objects.filter(status=True, article=article)

        return context


