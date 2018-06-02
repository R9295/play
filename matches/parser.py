import requests
from .models import Match

class MatchParser(object):

    def __init__(self, user, store_limit):
        self.user = user
        self.latest_match_id = self.get_latest_match_id()

    def get_latest_match_id():
        try:
            latest_match = list(Match.objects.filter(user=user, time_stamp__lt=now()))
            #latest_match.reverse()
            latest_match = latest_match[0].match_id
        except IndexError:
            latest_match = None
            matches, total_parsed = matchParser(latest_match, user)
