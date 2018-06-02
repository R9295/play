from django.db import models
import uuid
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

class Match(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4)
    time_stamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match_id = models.BigIntegerField()
    duration = models.IntegerField()
    first_blood_time = models.IntegerField()
    game_mode = models.CharField(max_length=25)
    user_win = models.BooleanField()
    patch = models.IntegerField()
    region = models.IntegerField()
    user_data = JSONField()
