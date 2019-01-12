from django.contrib import admin
from django.test import TestCase

from ..admin import HistoricalSiteAdmin
from ..models import HistoricalSite


class HistoricalSiteAdminTest(TestCase):
    def test_historical_site_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[HistoricalSite],
            HistoricalSiteAdmin
        )

    def test_historical_site_admin_should_set_list_display(self):
        expected = (
            'name',
            'community',
        )
        self.assertEqual(HistoricalSiteAdmin.list_display, expected)

    def test_historical_site_admin_should_set_list_filter(self):
        expected = (
            'community',
        )
        self.assertEqual(HistoricalSiteAdmin.list_filter, expected)

    def test_historical_site_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(HistoricalSiteAdmin.search_fields, expected)
