from django.test import TestCase
from ...models import UserManager



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {"username": "testuser", "password": "secret"}
        UserManager._create_user(**self.credentials)

    def test_login(self):
        # login
        response = self.client.post("/account/login/", **self.credentials)
        # should be logged in now, fails however
        self.assertTrue(response.context["user"].is_active)
