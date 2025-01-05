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
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(success_url="done"),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        views.CustomPasswordResetView.as_view(success_url="done"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
