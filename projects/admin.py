

from django.contrib import admin
from .models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'technologies', 'date_completed')
    list_filter = ('category', 'technologies', 'date_completed')
    search_fields = ('title', 'description', 'technologies')