from rest_framework.test import APITestCase
from django.urls import reverse
from src.models import User, Code


class TestSetup(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.profiles_url = reverse('profiles')
        self.login_url = reverse('login')

        self.user = User.objects.create_user(
            username="larry",
            email="larry.katuva@gmail.com",
            password="qazwsxedc"
        )
        self.user.is_verified = True
        self.user.save()
        self.login_data = {
            "username": "larry",
            "password": "qazwsxedc"
        }
        self.res = self.client.post(self.login_url, self.login_data)
        self.login_res = self.res.data
        self.token = self.login_res.get('tokens').get('access_token')
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
