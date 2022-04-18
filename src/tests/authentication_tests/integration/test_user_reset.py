from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import MockData
from src.models import User, Code
import pytest


@pytest.mark.django_db
class TestLoginViews(TestSetup):
    def test_request_password_reset_code(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        self.client.post(self.verify_email_url, data)
        reset_email = {
            'email': MockData().register_data1.get('email')
        }
        res = self.client.post(self.request_code_url, reset_email)
        self.assertEqual(res.data.get('message'), 'Reset code sent successfully. Please check your email')
        self.assertEqual(res.status_code, 200)

    def test_can_set_new_password(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        self.client.post(self.verify_email_url, data)
        reset_email = {
            'email': MockData().register_data1.get('email')
        }
        self.client.post(self.request_code_url, reset_email)
        user = User.objects.filter(email=MockData().register_data1.get('email'))[0]
        code = Code.objects.filter(user=user.id).order_by('-id')[:1][0]
        reset_data = {
            "code": code.code,
            "password": "qazwsxedc",
            "confirm_password": "qazwsxedc"
        }
        res = self.client.post(self.set_password_url, reset_data)
        self.assertEqual(res.data.get('message'), 'Password updated successfully')
        self.assertEqual(res.status_code, 201)
