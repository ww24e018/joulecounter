# counter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('add/', views.add_template, name='add_template'),
    path('log/', views.log_item, name='log_item'),
    path('summary/<int:days_back>/', views.daily_summary, name='daily_summary'),
]
