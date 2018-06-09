from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'home.html'

class PlayersView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'players.html'
