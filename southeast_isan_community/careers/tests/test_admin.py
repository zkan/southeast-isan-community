from django.contrib import admin
from django.test import TestCase

from ..admin import CareerAdmin
from ..models import Career


class CareerAdminTest(TestCase):
    def test_career_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[Career],
            CareerAdmin
        )

    def test_career_admin_should_set_list_display(self):
        expected = (
            'name',
            'community',
        )
        self.assertEqual(CareerAdmin.list_display, expected)

    def test_career_admin_should_set_list_filter(self):
        expected = (
            'community',
        )
        self.assertEqual(CareerAdmin.list_filter, expected)

    def test_career_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(CareerAdmin.search_fields, expected)
