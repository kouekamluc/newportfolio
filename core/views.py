
from django.views.generic import TemplateView
from .models import PersonalInfo, Education, WorkExperience
from projects.models import Project


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        context['education'] = Education.objects.all().order_by('-start_date')
        context['work_experience'] = WorkExperience.objects.all().order_by('-start_date')
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]  # Get up to 3 featured projects
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        context['education'] = Education.objects.all().order_by('-start_date')
        context['work_experience'] = WorkExperience.objects.all().order_by('-start_date')
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]  # Get up to 3 featured projects

        return context
