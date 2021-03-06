from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from matches.models import Match
from matches.serializers import MatchSerializer
from authentication.serializers import UserSerializer
from authentication.models import User
from user_profile.models import Server, Role, Hero, UserProfile
from invites.models import Invite
from invites.serializers import InviteSerializer
from user_profile.serializers import ServerSerializer, RoleSerializer, UserProfileSerializer, HeroSerializer
#from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
from rest_framework import status
from django.db.models import Q


class MatchApiView(ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(user=self.request.user)

class UserApiView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(profile=None, opendota_verified=False)
    @action(methods=['post'], detail=True)
    def profile(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            if user.profile == None:
                serializer = UserSerializer(data=request.data, instance=user, partial=True, context={'create':True})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                serializer = UserSerializer(data=request.data, instance=user, partial=True, context={'update':True})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error':'user not found'})

class ServerApiView(ReadOnlyModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class RoleApiView(ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class HeroApiView(ReadOnlyModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class InviteApiView(ModelViewSet):
    queryset = Invite.objects
    serializer_class = InviteSerializer

    def get_queryset(self):
        invites = Invite.objects.filter(Q(user_from=self.request.user) | Q(user_to=self.request.user))
        return invites
