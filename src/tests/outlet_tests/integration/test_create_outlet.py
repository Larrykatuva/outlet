from src.tests.outlet_tests.moc_data import MockData
from src.tests.outlet_tests.setup import TestSetup
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestOutletCreateViews(TestSetup):

    def test_cannot_create_outlet_while_not_logged_in(self):
        res = self.client.post(self.create_outlet, MockData().outlet_data)
        self.assertEqual(res.status_code, 401)

    def test_cannot_create_outlet_without_data(self):
        res = self.client.post(self.create_outlet, **self.auth_headers)
        self.assertEqual(res.status_code, 400)

    def test_can_create_outlet(self):
        res = self.client.post(self.create_outlet, MockData().outlet_data, **self.auth_headers)
        self.assertEqual(res.status_code, 201)
