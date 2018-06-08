from django.views.generic import TemplateView
from matches.models import Match
from authentication.models import User
from matches.serializers import MatchSerializer
from authentication.serializers import UserSerializer
import json

class HomeView(TemplateView):
    template_name = 'home.html'
    
class PlayersView(TemplateView):
    template_name = 'players.html'

    def get_context_data(self):
        context = super().get_context_data()
        players = User.objects.filter(opendota_verified=True)
        context['players'] = UserSerializer(players)
        return context
