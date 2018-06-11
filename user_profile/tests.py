from django.test import TestCase
from user_profile import models
from authentication.models import User
from django.db.utils import IntegrityError
from .serializers import UserProfileSerializer
from django.test import Client
import json
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
    # makes sure the serializer raises an exception if a profile exists for the user already
    def test_create_profile_twice(self):
        c.force_login(user=self.user)
        profile_data = {
            'user': self.user.id,
            'fav_servers': [1],
            'fav_roles':[1],
            'fav_heroes':[1,2],
        }
        c.post('/api/v1/profile/', profile_data, follow=True)
        self.assertEqual(models.UserProfile.objects.all().count(), 1)
        # again
        res = c.post('/api/v1/profile/', profile_data, follow=True)
        self.assertEqual(res.json()['user'][0], 'This field must be unique.')

    # makes sure errors are received if the choices supplied are over the limit for favourites
    # TODO push all this in one test
    def test_servers_over_limit(self):
        c.force_login(user=self.user)
        profile_data = {
            'user': self.user.id,
            'fav_servers': [1,2,3,4],
            'fav_roles':[1,2,3,4],
            'fav_heroes':[1,2,3,4,5,6],
        }
        res = c.post('/api/v1/profile/', profile_data, follow=True)
        self.assertEqual(res.json()['fav_servers'][0], 'Too many servers selected, maximum is 3')
        self.assertEqual(res.json()['fav_heroes'][0], 'Too many heroes selected, maximum is 5')
        self.assertEqual(res.json()['fav_roles'][0], 'Too many roles selected, maximum is 3')

    def test_put(self):
        #c.force_login(user=self.user)
        profile_data = {
            "user": str(self.user.id),
            "fav_servers": [1],
            "fav_roles":[1],
            "fav_heroes":[1,2],
        }
        print(profile_data)
        res = c.post('/api/v1/profile/', profile_data, follow=True)
        profile_data = {
            "user": str(self.user.id),
            "fav_servers": [1,2],
            "fav_roles":[1],
            "fav_heroes":[1,2],
        }
        profile_data = json.dumps(profile_data)
        res = c.put('/api/v1/profile/{}/'.format(res.json()['id']),profile_data, follow=True, content_type='application/json')
        print(res.json())
