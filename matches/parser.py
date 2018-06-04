import requests
from .models import Match
from django.utils.timezone import now
from django.conf import settings
from .rules import GameModeRules


player_field_list = [
    #'ability_upgrades_arr',
    'assists','camps_stacked','creeps_stacked','account_id','total_gold',
    #'damage',
    #'damage_inflictor',
    #'damage_taken',
    'deaths','denies','gold_per_min','actions_per_min','stuns',
    #'dn_t',
    ##'gold_reasons',
    'gold_spent','hero_damage','hero_healing','kill_streaks','hero_id',
    #'hero_i',
    #'killed',
    #'killed_by'
    'kills', 'last_hits', 'max_hero_hit', 'tower_damage', 'xp_per_min', 'isRadiant',
    'kills_per_min',
    'neutral_kills', 'roshan_kills', 'observer_uses', 'sentry_uses', 'lane',
    #'lane_role',
    'is_roaming',
]

class MatchObj(object):
    '''
    takes in:
    data = {
        match_id (int)
        duration  (int)
        first_blood_time (int)
        game_mode (int)
        radiant_win (bool)
        players  (json array with player_data dicts)
        patch  (int)
        region (int)
        user (django user instance)
    }
    '''
    def __init__(self, data):
        self.data = data
        self.parse()

    def find_user(self):
        player = None
        # finds the user
        for i in self.data['players']:
            if i['account_id'] is not None and int(i['account_id']) == self.data['user'].dotaid:
                player = i
        # extracts necessary user data
        self.data['user_data'] = {}
        for i in player_field_list:
            self.data['user_data'][i] = player.get(i)
        # remove unnecessary list
        self.data.pop('players', None)

    def parse_dota_api_ids(self):
        self.data['game_mode'] = GameModeRules.get(self.data['game_mode'])

    def parse_user_win(self):
        if self.data['user_data'].get('isRadiant') == True and self.data['radiant_win'] == True:
            self.data['user_win'] = True
        elif self.data['user_data'].get('isRadiant') == False and self.data['radiant_win'] == False:
            self.data['user_win'] = True
        # set to false if conditions not met
        self.data.setdefault('user_win', 'False')
        self.data.pop('radiant_win', None)
        self.data['user_data'].pop('isRadiant', None)

    def parse(self):
        self.find_user()
        self.parse_dota_api_ids()
        self.parse_user_win()

    def save(self):
        Match(**dict(self.data)).save()
        return self.data
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

    def parse_and_save(self):
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
            match = requests.get(settings.DOTA_API_URL+'/matches/{0}'.format(i['match_id'])).json()
            data = {
                'match_id': match['match_id'],
                'duration': match['duration'],
                'first_blood_time': match['first_blood_time'],
                'game_mode': match['game_mode'],
                'radiant_win': match['radiant_win'],
            #    'skill': match['skill'],
                'players': match['players'],
                'patch': match['patch'],
                'region': match['region'],
                'user': self.user
            }
            parsed_data = MatchObj(data=data)
            parsed_data.save()

    def clear_old_matches(self):
        if self.latest_match_id != None:
            matches = Match.objects.filter(user=user, time_stamp__lt=now())
            count = matches.count()
            matches = list(matches)
            matches.reverse()
            if len(matches) > settings.MATCH_STORE_LIMIT:
                for a in matches:
                    if count != MATCH_STORE_LIMIT:
                        a.delete()
                        count = count - 1
                    else:
                        self.total_deleted = count
                        break
