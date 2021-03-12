from django.urls import include, path
from .views import ContactUs



urlpatterns = [
    path('contact-us', ContactUs.as_view(), name='contact'),
]