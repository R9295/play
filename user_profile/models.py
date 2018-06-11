from django.db import models
from django.conf import settings
import uuid

class Server(models.Model):
    name = models.CharField(max_length=32)

class Hero(models.Model):
    name = models.CharField(max_length=32)

class Role(models.Model):
    name = models.CharField(max_length=32)

class UserProfile(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4)
    fav_servers = models.ManyToManyField(Server)
    fav_heroes = models.ManyToManyField(Hero)
    fav_roles = models.ManyToManyField(Role)
