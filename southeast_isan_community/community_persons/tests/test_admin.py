from django.contrib import admin
from django.test import TestCase

from ..admin import CommunityPersonAdmin
from ..models import CommunityPerson


class CommunityPersonAdminTest(TestCase):
    def test_community_admin_should_be_registered(self):
        self.assertIsInstance(
            admin.site._registry[CommunityPerson],
            CommunityPersonAdmin
        )

    def test_community_person_admin_should_set_list_display(self):
        expected = (
            'name',
            'community',
        )
        self.assertEqual(CommunityPersonAdmin.list_display, expected)

    def test_community_person_admin_should_set_list_filter(self):
        expected = (
            'community',
        )
        self.assertEqual(CommunityPersonAdmin.list_filter, expected)

    def test_community_person_admin_should_set_search_fields(self):
        expected = (
            'name',
        )
        self.assertEqual(CommunityPersonAdmin.search_fields, expected)
