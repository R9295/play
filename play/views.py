from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class PlayersView(TemplateView):
    template_name = 'players.html'
