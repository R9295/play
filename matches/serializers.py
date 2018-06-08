from rest_framework.serializers import ModelSerializer
from matches.models import Match

class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
