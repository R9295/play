from django.core.management.base import BaseCommand, CommandError
from authentication.models import User
from matches.tasks import updateMatches
class Command(BaseCommand):
    help = 'Updates all user matches'

    def handle(self, *args, **options):
        for i in User.objects.filter(opendota_verified=True):
            total_parsed, total_deleted = updateMatches(str(i.pk))
            self.stdout.write(self.style.SUCCESS('Deleted {0}; Parsed And Saved {1}; FOR {2}'.format(total_deleted, total_parsed, str(i.pk))))
