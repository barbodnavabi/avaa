from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import Q
from django.utils import timezone
from account.models import User
from translated_fields import TranslatedField
from django.utils.translation import gettext as _
from django.urls import reverse

class Tags(models.Model):
    title = TranslatedField(models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    article=models.ManyToManyField("Article")

    class Meta:
        verbose_name_plural = 'پرچسب ها'
        verbose_name = 'پرچسب '

    def get_absolute_url(self):
        return f'/articles/tag/{self.slug}'


STATUS_CHOICES = (
    ('d', 'پیش‌نویس'),  # draft
    ('p', "منتشر شده"),  # publish
    ('i', "در حال بررسی"),  # investigation
    ('b', "برگشت داده شده"),  # back
)

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def search_Article(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query)

        )
        return self.get_queryset().filter(lookup, status='p').distinct()

    def get_article_by_tag(self, tag_slug):
        return self.get_queryset().filter(tags__slug__iexact=tag_slug, status='p')


class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name="نویسنده")
    title = TranslatedField(models.CharField(max_length=200, verbose_name="عنوان مقاله"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    description = TranslatedField(RichTextUploadingField())
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name='مقاله'
        verbose_name_plural = 'مقاله ها '

    def __str__(self):
        return self.title

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})

        