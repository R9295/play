from rest_framework.viewsets import ReadOnlyModelViewSet
from matches.models import Match
from matches.serializers import MatchSerializer
from authentication.serializers import UsrSerializer
from authentication.models import User
class MatchApiView(ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(user=self.request.user)

class UserApiView(ReadOnlyModelViewSet):
    queryset = User.objects.filter(opendota_verified=True)
    serializer_class = UsrSerializer
