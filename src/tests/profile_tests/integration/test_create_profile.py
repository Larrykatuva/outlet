from src.tests.profile_tests.moc_data import MockData
from src.tests.profile_tests.setup import TestSetup
import pytest


@pytest.mark.django_db
class TestProfileCreateViews(TestSetup):

    def test_can_create_profile(self):
        res = self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        self.assertEqual(res.status_code, 201)

    def test_can_not_create_profile_without_data(self):
        res = self.client.post(self.profile_url, **self.auth_headers)
        self.assertEqual(res.status_code, 400)

    def test_cannot_create_profile_twice(self):
        self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        res = self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        self.assertEqual(res.status_code, 400)

