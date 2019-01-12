from django.test import TestCase

from ..models import HistoricSite
from communities.models import Community


class HistoricSiteTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.historic_site_name = 'วัดโสภณวิหาร'
        self.historic_site = HistoricSite.objects.create(
            name=self.historic_site_name,
            community=self.community
        )

    def test_historic_site_should_be_persisted_correctly(self):
        historic_site = HistoricSite.objects.last()
        self.assertEqual(historic_site.name, self.historic_site_name)
        self.assertEqual(historic_site.community.id, self.community.id)

    def test_historic_site_should_implement_str_for_friendly_name(self):
        self.assertEqual(
            self.historic_site.__str__(),
            self.historic_site_name
        )
