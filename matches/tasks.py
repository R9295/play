from huey.contrib.djhuey import task, periodic_task
from django.core.management import call_command
from .parser import MatchParser
from authentication.models import User
from django.conf import settings


@task()
def update_matches(user_pk):
    user = User.objects.get(pk=user_pk)
    parser = MatchParser(user=user, store_limit=settings.MATCH_STORE_LIMIT)
    parser.get_matches()
    parser.parse_and_save()
    parser.clear_old_matches()
    print('parsed and saved: '+ str(parser.total_parsed))
    print('deleted: '+ str(parser.total_deleted))
    return True

#@periodic_task(crontab(minute='0', hour='5'))
#def update_all_matches():
