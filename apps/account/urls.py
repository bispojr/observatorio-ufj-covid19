from django.urls import path, include
from .views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # to render a template html customized pass
    # template='template.html' into .as_view(),
    # so like: method.as_view(template_name='template.html')
    # By default has used adm reset django
    # samples:
    # template_name='registration/password_reset.html'
    # template_name='registration/password_reset_done.html'
    # template_name='registration/password_reset_confirm.html'
    # template_name='registration/password_reset_complete.html'
    path(
        "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
