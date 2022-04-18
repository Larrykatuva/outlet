from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import MockData
from src.models import User, Code
import pytest


@pytest.mark.django_db
class TestLoginViews(TestSetup):

    def test_cannot_login_without_data(self):
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code, 400)

    def test_cannot_login_with_wrong_username(self):
        self.client.post(self.register_url, MockData().register_data1)
        res = self.client.post(self.login_url, MockData().login_data2)
        self.assertEqual(res.data.get('username')[0], 'Username does not exits')
        self.assertEqual(res.status_code, 400)

    def test_cannot_login_unverified_user(self):
        self.client.post(self.register_url, MockData().register_data1)
        res = self.client.post(self.login_url, MockData().login_data1)
        self.assertEqual(res.data.get('email')[0], 'Email not verified')
        self.assertEqual(res.status_code, 400)

    def test_cannot_login_user_with_wrong_password(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        self.client.post(self.verify_email_url, data)
        wrong_data = {
            "username": "lawrence",
            "password": "tyuiii"
        }
        res = self.client.post(self.login_url, wrong_data)
        self.assertEqual(res.data.get('password')[0], 'Invalid login details')
        self.assertEqual(res.status_code, 400)

    def test_cannot_login_with_innactive_email(self):
        self.client.post(self.register_url, MockData().register_data1)
        User.objects.filter(email=MockData().register_data1.get('email')).update(is_active=False, is_verified=True)
        res = self.client.post(self.login_url, MockData().login_data1)
        self.assertEqual(res.data.get('email')[0], 'User account is inactive')
        self.assertEqual(res.status_code, 400)

    def test_can_login_user_with_correct_details(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        self.client.post(self.verify_email_url, data)
        res = self.client.post(self.login_url, MockData().login_data1)
        self.assertEqual(res.status_code, 200)
