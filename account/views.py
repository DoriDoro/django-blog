from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from account.forms import (
    RegistrationForm,
    CustomAuthenticationForm,
    UserEditForm,
)

UserModel = get_user_model()


class RegistrationView(CreateView):
    model = UserModel
    form_class = RegistrationForm
    template_name = "register/registration.html"
    success_url = reverse_lazy("account:dashboard")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class DashboardProfileView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = "profile/dashboard.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = "profile/user_edit.html"
    success_url = reverse_lazy("account:dashboard")

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    """Custom Password Reset View to add PROJECT_NAME to email the project name to user."""

    extra_email_context = {"PROJECT_NAME": settings.PROJECT_NAME}
