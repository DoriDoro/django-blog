from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from contact.forms import ContactRequestForm


class ContactRequestFormView(SuccessMessageMixin, FormView):
    form_class = ContactRequestForm
    template_name = "contact_form/contact.html"
    success_message = "Your message was sent."
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        try:
            form.send_email()
        except Exception as e:
            print("-- View error - Contact Form --", e)
            return HttpResponse("An error occurred in ContactRequestFormView")
        return super().form_valid(form)
