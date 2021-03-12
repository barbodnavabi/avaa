from .views import BlogListView,ArticleDetail
from django.urls import path

urlpatterns = [
    path('blog',BlogListView.as_view(),name='blog' ),
    path('blog/article/<slug:slug>',ArticleDetail.as_view(),name='blog-detail' ),

]
