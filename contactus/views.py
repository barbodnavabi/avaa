from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contactus
from django.urls import reverse_lazy

# Create your views here.
class ContactUs(CreateView):
    model = Contactus
    template_name ='contact/contact-us.html'
    success_url=reverse_lazy('index')
    fields=["full_name","email","subject","phone","text",]
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context    
