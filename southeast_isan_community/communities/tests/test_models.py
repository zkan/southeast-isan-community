from django.test import TestCase

from ..models import Community


class CommunityTest(TestCase):
    def setUp(self):
        self.community_name = 'ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        self.community_regional_dialect = 'โอะโยะ'
        self.community_faith = 'ภูตผี'
        self.community_folk_game = 'มอญซ่อนผ้า'
        self.community = Community.objects.create(
            name=self.community_name,
            regional_dialect=self.community_regional_dialect,
            faith=self.community_faith,
            folk_game=self.community_folk_game
        )

    def test_community_should_be_persisted_correctly(self):
        community = Community.objects.last()
        self.assertEqual(community.name, self.community_name)
        self.assertEqual(
            community.regional_dialect,
            self.community_regional_dialect
        )
        self.assertEqual(community.faith, self.community_faith)
        self.assertEqual(community.folk_game, self.community_folk_game)

    def test_community_should_show_correct_plural_name(self):
        self.assertEqual(
            self.community._meta.verbose_name_plural,
            'communities'
        )

    def test_community_should_implement_str_for_friendly_name(self):
        self.assertEqual(self.community.__str__(), self.community_name)
