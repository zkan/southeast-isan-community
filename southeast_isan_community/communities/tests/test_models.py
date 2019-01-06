from django.test import TestCase

from ..models import Community


class CommunityTest(TestCase):
    def test_save_community(self):
        community = Community()
        community.name = 'ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        community.save()

        community = Community.objects.last()

        expected = 'ชุมชนบ้านเชื้อเพลิง (Chueaploeng Community)'
        self.assertEqual(community.name, expected)
