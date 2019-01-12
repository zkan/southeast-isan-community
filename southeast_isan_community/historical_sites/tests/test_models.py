from django.test import TestCase

from ..models import HistoricalSite
from communities.models import Community


class HistoricalSiteTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.historical_site_name = 'วัดโสภณวิหาร'
        self.historical_site = HistoricalSite.objects.create(
            name=self.historical_site_name,
            community=self.community
        )

    def test_historical_site_should_be_persisted_correctly(self):
        historical_site = HistoricalSite.objects.last()
        self.assertEqual(historical_site.name, self.historical_site_name)
        self.assertEqual(historical_site.community.id, self.community.id)

    def test_historical_site_should_implement_str_for_friendly_name(self):
        self.assertEqual(
            self.historical_site.__str__(),
            self.historical_site_name
        )
