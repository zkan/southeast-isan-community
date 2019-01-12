from django.test import TestCase

from ..models import NaturalPlace
from communities.models import Community


class NaturalPlaceTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.natural_place_name = 'บารายทะเลเมืองต่ำ'
        self.natural_place = NaturalPlace.objects.create(
            name=self.natural_place_name,
            community=self.community
        )

    def test_natural_place_should_be_persisted_correctly(self):
        natural_place = NaturalPlace.objects.last()
        self.assertEqual(natural_place.name, self.natural_place_name)
        self.assertEqual(natural_place.community.id, self.community.id)

    def test_natural_place_should_implement_str_for_friendly_name(self):
        self.assertEqual(self.natural_place.__str__(), self.natural_place_name)
