
from django.views.generic import TemplateView
from .models import PersonalInfo, Education, WorkExperience

class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        context['education'] = Education.objects.all().order_by('-start_date')
        context['work_experience'] = WorkExperience.objects.all().order_by('-start_date')
        return context
