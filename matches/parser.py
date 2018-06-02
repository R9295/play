import requests
from .models import Match
from django.utils.timezone import now
from django.conf import settings

class MatchParser(object):

    def __init__(self, user, store_limit):
        self.user = user
        self.latest_match_id = self.get_latest_match_id()
        self.store_limit = store_limit

    def get_latest_match_id(self):
        try:
            latest_match = list(Match.objects.filter(user=self.user, time_stamp__lt=now()))
            #latest_match.reverse()
            return latest_match[0].match_id
        except IndexError:
            return None

    def get_matches(self):
        self.matches = requests.get(settings.DOTA_API_URL+'/players/{0}/matches?limit={1}'.format(self.user.dotaid, self.store_limit)).json()

    def parse_step_one(self):
        '''
            Takes matches and returns only the ones that needed to be parsed(filters using latest_match_id)
            requeries opendota and only necessary the fields the json are passed on.
        '''
        self.parsed = []
        self.total_parsed = 0
        for i in self.matches:
            if i['match_id'] == self.latest_match_id:
                break
            self.total_parsed = self.total_parsed + 1
            match = requests.get(DOTA_API_URL+'/matches/{0}'.format(i['match_id'])).json()
            data = {
                'match_id': match['match_id'],
                'duration': match['duration'],
                'first_blood_time': match['first_blood_time'],
                'game_mode': match['game_mode'],
                'radiant_win': match['radiant_win'],
                'skill': match['skill'],
                'players': match['players'],
                'patch': match['patch'],
                'region': match['region'],
            }
            self.parsed.append(data)
            
    def parse_matches(self):
        self.parse_step_one()
