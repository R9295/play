from django.test import TestCase
from user_profile import models
from authentication.models import User
from django.db.utils import IntegrityError
from .serializers import UserProfileSerializer
from django.test import Client
import json
from unittest import skip


c = Client()
class UserProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        heroes = [
            {'name': 'Morphling'},
            {'name': 'Kunkka'},
            {'name': 'Tinker'},
            {'name': 'Sniper'},
            {'name': 'Zeus'},
            {'name': 'Slark'},
        ]
        roles = [
            {'name':'Carry'},
            {'name':'Support'},
            {'name':'Mid'},
            {'name':'Offlane'},
        ]
        servers = [
            {'name':'Russia'},
            {'name':'India'},
            {'name':'SEA'},
            {'name':'EU West'},
            {'name':'EU East'},
            {'name':'US West'},
            {'name':'US East'},
        ]

        for i in heroes:
            models.Hero.objects.create(**i).save()
        for i in roles:
            models.Role.objects.create(**i).save()
        for i in servers:
            models.Server.objects.create(**i).save()
        cls.user = User.objects.create(steamid='76561198232898112')

    def test_create_profile(self):
        c.force_login(user=self.user)
        profile_data = {
            "user": str(self.user.pk),
            "profile": {
                "fav_servers": ["Russia"],
                "fav_roles":["Carry"],
                "fav_heroes":["Slark","Zeus"],
            },
        }
        f = c.post('/api/v1/users/{}/profile/'.format(str(self.user.id)),json.dumps(profile_data), content_type='application/json',follow=True)
        self.assertEqual(models.UserProfile.objects.all().count(), 1)

    # makes sure errors are received if the choices supplied are over the limit for favourites
    # TODO push all this in one test
    def test_servers_over_limit(self):
        c.force_login(user=self.user)
        profile_data = {
            'user': str(self.user.id),
            'profile':{
                'fav_servers': ["Russia","EU West","India","SEA"],
                'fav_roles':["Carry","Mid","Offlane","Support"],
                'fav_heroes':["Kunkka", "Slark", "Zeus", "Sniper", "Tinker", "Morphling"],
            }
        }
        res = c.post('/api/v1/users/{}/profile/'.format(str(self.user.id)),json.dumps(profile_data), content_type='application/json',follow=True)
        res = res.json()['profile']
        self.assertEqual(res['fav_servers'][0], 'Too many servers selected, maximum is 3')
        self.assertEqual(res['fav_heroes'][0], 'Too many heroes selected, maximum is 5')
        self.assertEqual(res['fav_roles'][0], 'Too many roles selected, maximum is 3')

    def test_update(self):
        #c.force_login(user=self.user)
        profile_data = {
            "user": str(self.user.pk),
            "profile": {
                "fav_servers": ["Russia"],
                "fav_roles":["Carry"],
                "fav_heroes":["Slark","Zeus"],
            },
        }
        res = c.post('/api/v1/users/{}/profile/'.format(str(self.user.id)),json.dumps(profile_data), content_type='application/json',follow=True)
        profile_data = {
            "user": str(self.user.pk),
            "profile": {
                "fav_servers": ["Russia",'SEA'],
                "fav_roles":["Carry"],
                "fav_heroes":["Slark","Zeus"],
            },
        }
        res = c.post('/api/v1/users/{}/profile/'.format(str(self.user.id)),json.dumps(profile_data), content_type='application/json',follow=True)
        self.assertEqual(res.json()['profile']['fav_servers'], ['Russia','SEA'])
