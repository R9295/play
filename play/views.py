from django.views.generic import TemplateView
from matches.models import Match
from matches.serializers import MatchSerializer
import json


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = super().get_context_data()
        matches = Match.objects.filter(user=self.request.user)
        context['matches'] = MatchSerializer(matches)
        return context
