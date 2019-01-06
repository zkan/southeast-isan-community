from django.contrib import admin
from django.test import TestCase

from ..admin import CommunityAdmin
from ..models import Community


class CommunityAdminTest(TestCase):
    def test_community_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[Community],
            CommunityAdmin
        )

    def test_community_admin_should_set_list_display(self):
        expected = (
            'name',
        )
        self.assertEqual(CommunityAdmin.list_display, expected)

    def test_community_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(CommunityAdmin.search_fields, expected)
