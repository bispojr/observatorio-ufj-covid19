from django.test import TestCase
from django.test import Client

# Create your tests here.

class AcessosViewTestCase(TestCase):

    def test_status_code_200(self):
        c = Client()
        response = c.post('/')
        self.assertEquals(response.status_code, 200)
