from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import MockData
from src.models import User, Code
import pytest


@pytest.mark.django_db
class TestRegisterViews(TestSetup):

    def test_cannot_register_user_without_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_can_register_user(self):
        res = self.client.post(self.register_url, MockData().register_data1)
        self.assertEqual(res.status_code, 201)

    def test_cannot_register_existing_user(self):
        self.client.post(self.register_url, MockData().register_data1)
        res = self.client.post(self.register_url, MockData().register_data1)
        self.assertEqual(res.status_code, 400)

    def test_cannot_verify_unavailable_user(self):
        data = {"code": "RGE$F"}
        res = self.client.post(self.verify_email_url, data)
        self.assertEqual(res.data.get('code')[0], 'Invalid verification code')
        self.assertEqual(res.status_code, 400)

    def test_cannot_use_verification_code_twice(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        self.client.post(self.verify_email_url, data)
        res = self.client.post(self.verify_email_url, data)
        self.assertEqual(res.data.get('code')[0], 'Verification code already used')
        self.assertEqual(res.status_code, 400)


    def test_can_verify_user(self):
        self.client.post(self.register_url, MockData().register_data1)
        user = User.objects.filter(email=MockData().register_data1.get('email'))
        code = Code.objects.get(user=user[0].id)
        data = {"code": code.code}
        res = self.client.post(self.verify_email_url, data)
        self.assertEqual(res.status_code, 201)

