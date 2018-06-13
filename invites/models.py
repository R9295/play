from django.db import models
from authentication.models import User


class Invite(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invite_to')
    time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='awating_response', max_length=30)
