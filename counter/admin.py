from django.contrib import admin
from .models import FoodItemTemplate, FoodItemLog

@admin.register(FoodItemTemplate)
class FoodItemTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'modifier', 'joules')
    list_filter = ('name',)
    search_fields = ('name', 'modifier')

@admin.register(FoodItemLog)
class FoodItemLogAdmin(admin.ModelAdmin):
    list_display = ('template', 'eaten_at')
    list_filter = ('eaten_at',)
    date_hierarchy = 'eaten_at'
