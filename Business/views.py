from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Agents
class AgentsListView(ListView):
    model = Agents
    template_name = "business/agents-list.html"
    queryset=Agents.objects.all()

# Create your views here.
class AgentsDetailView(DetailView):
    model = Agents
    template_name = "business/agents-detail.html"
