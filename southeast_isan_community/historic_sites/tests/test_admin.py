from django.contrib import admin
from django.test import TestCase

from ..admin import HistoricSiteAdmin
from ..models import HistoricSite


class HistoricSiteAdminTest(TestCase):
    def test_historic_site_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[HistoricSite],
            HistoricSiteAdmin
        )

    def test_historic_site_admin_should_set_list_display(self):
        expected = (
            'name',
            'community',
        )
        self.assertEqual(HistoricSiteAdmin.list_display, expected)

    def test_historic_site_admin_should_set_list_filter(self):
        expected = (
            'community',
        )
        self.assertEqual(HistoricSiteAdmin.list_filter, expected)

    def test_historic_site_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(HistoricSiteAdmin.search_fields, expected)
