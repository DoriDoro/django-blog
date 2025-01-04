from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django import forms

UserModel = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Email Address",
                "aria-label": "Your Email Address",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter a username",
                "aria-label": "Enter a username",
            }
        )
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Your first name",
                "aria-label": "Your first name",
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Your last name",
                "aria-label": "Your last name",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter a secure password",
                "aria-label": "Enter a secure password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Repeat your password",
                "aria-label": "Repeat your password",
            }
        )
        self.fields["introduction"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": 4,
                "placeholder": "Introduce yourself in a few words...",
                "aria-label": "Introduce yourself in a few words...",
            }
        )

    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "introduction",
        ]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
                "aria-label": "Enter your username",
                "autofocus": True,
            }
        ),
        label="",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
                "aria-label": "Enter your password",
                "autocomplete": "current-password",
            }
        ),
        label="",
        strip=False,
    )


class UserEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Update your username",
                "aria-label": "Update your username",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Update your Email Address",
                "aria-label": "Update your Email Address",
            }
        )
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Update your first name",
                "aria-label": "Update your first name",
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Update your last name",
                "aria-label": "Update your last name",
            }
        )
        self.fields["introduction"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": 6,
                "placeholder": "Update to introduce yourself in a few words...",
                "aria-label": "Update to introduce yourself in a few words...",
            }
        )

    class Meta:
        model = UserModel
        fields = ["username", "email", "first_name", "last_name", "introduction"]
