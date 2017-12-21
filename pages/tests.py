from django.test import SimpleTestCase
from django.test import TestCase

# Create your tests here.

class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)