from django.forms.models import model_to_dict
import datetime
import json

def MatchSerializer(matches):
    match_list = []
    for i in matches:
        match = model_to_dict(i)
        match['id'] = str(match['id'])
        match['time_stamp'] = match['time_stamp'].strftime("%Y-%m-%d")
        match['user_win'] = str(match['user_win'])
        match_list.append(match)
    return json.dumps(match_list)
