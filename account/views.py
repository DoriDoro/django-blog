from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from account.forms import RegistrationForm, CustomAuthenticationForm

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
