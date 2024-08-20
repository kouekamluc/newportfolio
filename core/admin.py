from django.contrib import admin

# Register your models here.
from .models import PersonalInfo, Education, WorkExperience

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(WorkExperience)