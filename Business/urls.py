from django.urls import path
from .views import AgentsListView,AgentsDetailView
urlpatterns = [
    path('agents',AgentsListView.as_view(),name='agents'),
    path('agents/<int:pk>',AgentsDetailView.as_view(),name='agent-detail')
]
