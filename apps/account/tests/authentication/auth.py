from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from .manager import UsersManagersTests


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
        user = authenticate(username="deolhonocoronga@example.com", password="123456")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username="deolhonocorona@example.com", password="1234567")
        self.assertFalse(user is not None and user.is_authenticated)


class SignInViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="deolhonocorona@example.com", password="123456"
        )

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post(
            "/account/login/", {"email": "deolhonocorona@example.com", "password": "1234567"}
        )
        self.assertTrue(response["authenticated"] is True)

    # def test_wrong_username(self):
    #     response = self.client.post(
    #         "/signin/", {"username": "wrong", "password": "12test12"}
    #     )
    #     self.assertFalse(response.data["authenticated"])
    #
    # def test_wrong_pssword(self):
    #     response = self.client.post(
    #         "/signin/", {"username": "test", "password": "wrong"}
    #     )
    #     self.assertFalse(response.data["authenticated"])
