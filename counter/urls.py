# counter/urls.py
from django.urls import path
from . import views
from .models import FoodItemTemplate

urlpatterns = [
    path('', views.overview, name='overview'),
    path('add/', views.add_template, name='add_template'),
    path('log/', views.log_item, name='log_item'),
    path('summary/<int:days_back>/', views.daily_summary, name='daily_summary'),
    path('itemtemp/export/', FoodItemTemplate.export_view, name='food_export'),
    path('itemtemp/import/', FoodItemTemplate.import_view, name='food_import'),
]
