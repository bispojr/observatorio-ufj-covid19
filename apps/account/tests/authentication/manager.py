from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from ...models import UserManager


class UsersManagersTests(TestCase):
    """Test if model has work OK to create User and SuperUser."""

    def test_create_user(self, email, password):
        """Return the User model that is active in this project."""
        User = get_user_model()
        user = User.objects.create_user(email=email, password=password)

        """Fail if the two objects are unequal by determined."""
        self.assertEqual(user.email, "user@user.com")
        self.assertTrue(user.is_active)
        try:
            """
            Username is None for the AbstractUser option
            Username does not exist for the AbstractBaseUser option
            """
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password=password)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser("super@user.com", "super_pass")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            """
            Username is None for the AbstractUser option
            Username does not exist for the AbstractBaseUser option
            """
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="super_pass", is_superuser=False
            )
