from django.test import TestCase
from .models import Match
from authentication.models import User
from .parser import MatchParser
from django.conf import settings
from unittest import skip
from django.utils.timezone import now


# THE TESTS WITH SKIP TAKE A WHILE(query apis, parse ,etc), TEST ONLY WHEN NEEDED
class MatchTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(steamid='76561198232898112')

    @skip
    def test_match_parser(self):
        parser = MatchParser(user=self.user,store_limit=settings.TEST_STORE_LIMIT)
        self.assertEqual(parser.latest_match_id, None)

    #@skip
    def test_get_matches(self):
        parser = MatchParser(user=self.user,store_limit=settings.TEST_STORE_LIMIT)
        parser.get_matches()
        self.assertEqual(len(parser.matches), 5)
        parser.parse_and_save()
        self.assertEqual(Match.objects.filter(user=self.user).count(), 5)
