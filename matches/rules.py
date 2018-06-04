from django.conf import settings
import json


GameModeRules={
    0:'Unknown',
    1:'AllPick',
    2:'Captain’sMode',
    3:'RandomDraft',
    4:'SingleDraft',
    5:'AllRandom',
    6:'Intro',
    7:'Diretide',
    8:'ReverseCaptain’sMode',
    9:'TheGreeviling',
    10:'Tutorial',
    11:'MidOnly',
    12:'LeastPlayed',
    13:'NewPlayerPool',
    14:'CompendiumMatchmaking',
    15:'Custom',
    16:'CaptainsDraft',
    17:'BalancedDraft',
    18:'AbilityDraft',
    19:'Event(?)',
    20:'AllRandomDeathMatch',
    21:'SoloMid1vs1',
    22:'RankedAllPick',
}

def get_hero(id):
    with open(settings.BASE_DIR+'/matches/heroes.json') as heroes:
        data = json.load(heroes)
        hero = None
        for i in data['heroes']:
            if i['id'] == id:
                hero = i['localized_name']
        return hero
