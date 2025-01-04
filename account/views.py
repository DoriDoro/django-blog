from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegistrationForm

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
