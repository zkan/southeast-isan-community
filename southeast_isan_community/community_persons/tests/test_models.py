from django.test import TestCase

from ..models import CommunityPerson
from communities.models import Community


class CommunityPersonTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.community_person_name = 'นายเพียร สุขใจ'
        self.community_person = CommunityPerson.objects.create(
            name=self.community_person_name,
            community=self.community
        )

    def test_community_person_should_be_persisted_correctly(self):
        expected = self.community_person_name
        community_person = CommunityPerson.objects.last()
        self.assertEqual(community_person.name, expected)
        self.assertEqual(community_person.community.id, self.community.id)

    def test_community_should_implement_str_for_friendly_name(self):
        expected = self.community_person_name
        self.assertEqual(self.community_person.__str__(), expected)
