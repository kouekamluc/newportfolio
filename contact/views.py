from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your message has been sent successfully. Thank you for contacting me!")
        return response