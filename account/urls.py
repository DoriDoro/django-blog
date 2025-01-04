from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("profile/", views.DashboardProfileView.as_view(), name="dashboard"),
    path("edit-profile/", views.UserEditView.as_view(), name="edit_profile"),
]
