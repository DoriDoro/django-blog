from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
