from django.contrib import admin

# Register your models here.
from .models import Tags,Article
admin.site.register(Tags)
admin.site.register(Article)