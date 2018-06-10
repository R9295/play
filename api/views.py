from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from matches.models import Match
from matches.serializers import MatchSerializer
from authentication.serializers import UsrSerializer
from authentication.models import User
from user_profile.models import Server, Role, Hero, UserProfile
from user_profile.serializers import ServerSerializer, RoleSerializer, UserProfileSerializer, HeroSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
class MatchApiView(ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(user=self.request.user)

class UserApiView(ReadOnlyModelViewSet):
    queryset = User.objects.filter(opendota_verified=True)
    serializer_class = UsrSerializer

    @action(methods=['GET'], detail=True)
    def profile(self, request, pk=None):
        try:
            profile = UserProfile.objects.get(user=pk)
        except (ValidationError, UserProfile.DoesNotExist):
            return Response({'error':'This user does not have a profile'})
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

class ServerApiView(ReadOnlyModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class RoleApiView(ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class HeroApiView(ReadOnlyModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class ProfileApiView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
