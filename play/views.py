from django.views.generic import TemplateView


class HomeView(TemplateView):
    template = 'index.html'
