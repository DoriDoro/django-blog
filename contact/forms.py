from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from contact.models import ContactRequest


UserModel = get_user_model()


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        exclude = ["submitted_at", "customer_feedback"]
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "subject": "",
            "message": "",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your First name",
                    "aria-label": "Your First name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Last name",
                    "aria-label": "Your Last name",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Email Address",
                    "aria-label": "Your Email Address",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the subject",
                    "aria-label": "Enter the subject",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Your message",
                    "aria-label": "Your message",
                }
            ),
        }

    def send_email(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data.get(
            "last_name", None
        )  # last_name is not mandatory
        name = first_name if last_name is None else f"{first_name} {last_name}"
        subject = self.cleaned_data["subject"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        create_message = f"""
            Received a message from 
            Name: {name}
            Email: {email} 
            with Subject: {subject}
            ----------------
            
            {message} 
            """

        try:
            send_mail(
                subject=f"Contact Form submission: {settings.PROJECT_NAME}",
                message=create_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL.strip()],
            )
        except Exception as e:
            print(
                "--- ERROR - FAILED Contact Form submission---",
                "email of sender: ",
                email,
                " ---> Error message: ",
                e,
            )
            raise
