from rest_framework.test import APITestCase
from src.tests.authentication_tests.moc_data import MockData
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self):
        self.mock_data = MockData()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.request_code_url = reverse('request-code')
        self.set_password_url = reverse('set-new-password')
        self.verify_email_url = reverse('verify-email')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
