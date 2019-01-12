from django.contrib import admin
from django.test import TestCase

from ..admin import NaturalPlaceAdmin
from ..models import NaturalPlace


class NaturalPlaceAdminTest(TestCase):
    def test_natural_place_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[NaturalPlace],
            NaturalPlaceAdmin
        )

    def test_natural_place_admin_should_set_list_display(self):
        expected = (
            'name',
            'community',
        )
        self.assertEqual(NaturalPlaceAdmin.list_display, expected)

    def test_natural_place_admin_should_set_list_filter(self):
        expected = (
            'community',
        )
        self.assertEqual(NaturalPlaceAdmin.list_filter, expected)

    def test_natural_place_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(NaturalPlaceAdmin.search_fields, expected)
