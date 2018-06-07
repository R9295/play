from huey.contrib.djhuey import task, periodic_task
from django.core.management import call_command
from .parser import MatchParser
from authentication.models import User
from django.conf import settings


def updateMatches(user_pk):
    user = User.objects.get(pk=user_pk)
    parser = MatchParser(user=user, store_limit=settings.MATCH_STORE_LIMIT)
    parser.get_matches()
    print('got matches')
    parser.parse_and_save()
    print('finished pasing and saving')
    parser.clear_old_matches()
    print('clearing old')
    return parser.total_parsed, parser.total_deleted

@task()
def update_matches(user_pk):
    updateMatches(user_pk)
    return True
