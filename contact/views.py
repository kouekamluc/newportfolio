from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the contact form data
        contact = form.save()
        
        # Send email
        subject = f"New contact form submission: {contact.subject}"
        message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        # Add success message
        messages.success(self.request, 'Your message has been sent successfully!')
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your submission. Please check the form and try again.')
        return super().form_invalid(form)