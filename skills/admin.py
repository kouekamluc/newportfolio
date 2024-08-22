

from django.contrib import admin
from .models import SkillCategory, Skill

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','order')
    list_editable = ('order',)



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'years_of_experience', 'icon')
    list_filter = ('category', 'proficiency')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'proficiency', 'years_of_experience')
        }),
        ('Icon', {
            'fields': ('icon',),
            'description': 'Enter a Font Awesome icon class (e.g., "fas fa-code"). You can find icons at https://fontawesome.com/icons'
        }),
    )