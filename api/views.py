from rest_framework.viewsets import ReadOnlyModelViewSet
from matches.models import Match
from matches.serializers import MatchSerializer


class MatchApiView(ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(user=self.request.user)
