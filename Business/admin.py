from django.contrib import admin

# Register your models here.
from .models import Brands,Agents

admin.site.register(Brands)
admin.site.register(Agents)