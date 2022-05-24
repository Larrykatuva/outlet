from src.tests.outlet_tests.moc_data import MockData
from src.tests.outlet_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestOutletCreateViews(TestSetup):

    def test_can_get_all_outlets(self):
        self.client.post(self.create_outlet, MockData().outlet_data, **self.auth_headers)
        res = self.client.get(self.list_outlets, **self.auth_headers)
        self.assertEqual(res.status_code, 200)

    def test_can_get_outlet_by_id(self):
        res = self.client.post(self.create_outlet, MockData().outlet_data, **self.auth_headers)
        outlet = self.client.get(reverse('outlet', args=[res.data.get('id')]), **self.auth_headers)
        self.assertEqual(outlet.status_code, 200)

    def test_can_update_outlet(self):
        res = self.client.post(self.create_outlet, MockData().outlet_data, **self.auth_headers)
        update_data = {
            "name": "Katuva"
        }
        outlet = self.client.patch(reverse('outlet', args=[res.data.get('id')]), update_data, **self.auth_headers)
        self.assertEqual(outlet.status_code, 200)



