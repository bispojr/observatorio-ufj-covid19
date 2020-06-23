import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib import auth
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        verbose_name="Identifier Unique", default=uuid.uuid4, editable=False
    )
    email = models.EmailField(null=False, verbose_name="E-mail", unique=True)
    full_name = models.CharField(
        max_length=50, null=True, verbose_name="Full name", default=None
    )
    password = models.CharField(_("password"), max_length=128)
    username = models.CharField(max_length=512, blank=True, null=True, default=None)
    is_active = models.BooleanField(_("Active"), null=False, blank=False, default=True)
    is_staff = models.BooleanField(_("staff status"), default=True)

    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def login(request):
        msg_return = ""
        is_logged = False
        try:
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            if request.method == "POST":
                u = User.objects.filter(email=email)
                u_count = u.count()
                if u_count == 1:
                    session = auth.authenticate(email=email, password=password)
                    if session:
                        auth.login(request, session)
                        is_logged = True
                    else:
                        msg_return = "invalid_credentials"
                else:
                    msg_return = "not_found"
        except:
            return request, msg_return, is_logged
        return request, msg_return, is_logged

    # def logout(request):
    #     auth.logout(request)
    #     return redirect("accounts:login")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"