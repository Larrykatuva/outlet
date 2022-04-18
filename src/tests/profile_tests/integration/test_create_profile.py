from src.tests.profile_tests.moc_data import MockData
from src.tests.profile_tests.setup import TestSetup
import pytest


@pytest.mark.django_db
class TestProfileViews(TestSetup):

    def test_can_create_profile(self):
        res = self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        print(self.auth_headers)
        print(res.data)
        self.assertEqual(res.status_code, 201)
