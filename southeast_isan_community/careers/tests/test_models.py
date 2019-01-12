from django.test import TestCase

from ..models import Career
from communities.models import Community


class CareerTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.career_name = 'ทอเสื่อกกยกลาย'
        self.career = Career.objects.create(
            name=self.career_name,
            community=self.community
        )

    def test_career_should_be_persisted_correctly(self):
        career = Career.objects.last()
        self.assertEqual(career.name, self.career_name)
        self.assertEqual(career.community.id, self.community.id)

    def test_career_should_implement_str_for_friendly_name(self):
        self.assertEqual(self.career.__str__(), self.career_name)
