from src.tests.profile_tests.moc_data import MockData
from src.tests.profile_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestProfileGetViews(TestSetup):

    def test_can_get_profile_by_id(self):
        res = self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        profile = self.client.get(reverse('user-profile', args=[res.data.get('id')]), **self.auth_headers)
        self.assertEqual(profile.status_code, 200)

    def test_can_get_all_profiles(self):
        res = self.client.get(self.profiles_url, **self.auth_headers)
        self.assertEqual(res.status_code, 200)

    def test_can_update_profile(self):
        res = self.client.post(self.profile_url, MockData().profile_data1, **self.auth_headers)
        update_data = {
            'phone': '0720460519'
        }
        profile = self.client.patch(reverse('user-profile', args=[res.data.get('id')]), update_data,
                                    **self.auth_headers)
        self.assertEqual(profile.status_code, 200)

