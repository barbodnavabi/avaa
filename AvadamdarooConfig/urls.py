from django.urls import path

from AvadamdarooConfig.views import Index

urlpatterns = [
    path('', Index,name='index'),

]
