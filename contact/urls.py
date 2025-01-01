from django.urls import path

from contact.views import ContactRequestFormView

app_name = "contact"

urlpatterns = [
    path("", ContactRequestFormView.as_view(), name="contact_me"),
]
