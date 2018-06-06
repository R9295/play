from django.views.generic import TemplateView
from matches.models import Match
from authentication.models import User
from matches.serializers import MatchSerializer
from authentication.serializers import UserSerializer
import json


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = super().get_context_data()
        matches = Match.objects.filter(user=self.request.user)
        context['matches'] = MatchSerializer(matches)
        return context

class PlayersView(TemplateView):
    template_name = 'players.html'

    def get_context_data(self):
        context = super().get_context_data()
        players = User.objects.filter(opendota_verified=True)
        context['players'] = UserSerializer(players)
        #context['players'] = json.dumps([{'pk':'pk', 'personaname':'123'}])
        return context
