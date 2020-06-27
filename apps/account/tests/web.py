from django.test import Client
from django.contrib.auth import get_user_model
from django.test import TestCase


class SignInViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="deolhonocorona@example.com", password="123456"
        )

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        c = Client()
        response = c.post("/account/login/", {"email": "deolhonocorona@example.com", "password": "123456"})
        self.assertEqual(response.status_code, 200)

    def test_wrong_username(self):
        c = Client()
        response = c.post("/account/login/", {"email": "deolhonocoronas@example.com", "password": "123456"})
        self.assertEqual(response.status_code, 401)

    def test_wrong_pssword(self):
        c = Client()
        response = c.post("/account/login/", {"email": "deolhonocorona@example.com", "password": "1234567"})
        self.assertEqual(response.status_code, 401)


class LogoutTest(TestCase):
   def test_logout(self):
        self.client = Client()
        self.client.login(email="deolhonocorona@example.com", password="123456")
        response = self.client.get("/account/logout/")
        self.assertEqual(response.status_code, 200)
