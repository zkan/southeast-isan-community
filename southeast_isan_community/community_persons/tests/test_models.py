from django.test import TestCase

from ..models import CommunityPerson
from communities.models import Community


class CommunityPersonTest(TestCase):
    def setUp(self):
        self.community = Community.objects.create(
            name='ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        )
        self.community_person_name = 'นายเพียร สุขใจ'
        self.community_person_role = 'leader'
        self.community_person = CommunityPerson.objects.create(
            name=self.community_person_name,
            role=self.community_person_role,
            community=self.community
        )

    def test_community_person_should_be_persisted_correctly(self):
        community_person = CommunityPerson.objects.last()
        self.assertEqual(community_person.name, self.community_person_name)
        self.assertEqual(community_person.role, self.community_person_role)
        self.assertEqual(community_person.community.id, self.community.id)

    def test_community_person_should_implement_str_for_friendly_name(self):
        expected = f'{self.community_person_name} ' \
            f'({self.community_person_role})'
        self.assertEqual(self.community_person.__str__(), expected)
