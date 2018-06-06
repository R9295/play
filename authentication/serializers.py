from django.forms.models import model_to_dict
import datetime
import json

def UserSerializer(users):
    user_list = []
    for i in users:
        user = model_to_dict(i)
        user['id'] = str(user['id'])
        user.pop('password', None)
        user['date_joined'] = user['date_joined'].strftime("%Y-%m-%d")
        user['last_login'] = user['last_login'].strftime("%Y-%m-%d")
        user_list.append(user)
    return json.dumps(user_list)
