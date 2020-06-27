from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class SignInTest(TestCase):
    """Test if model has work OK to create User and Login method."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="deolhonocorona@example.com", password="123456"
        )

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = auth.authenticate(email="deolhonocorona@example.com", password="123456")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username="deolhonocoronas@example.com", password="123456")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username="deolhonocorona@example.com", password="1234567")
        self.assertFalse(user is not None and user.is_authenticated)
