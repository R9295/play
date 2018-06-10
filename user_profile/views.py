from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'profile.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['user'] = str(self.request.user.id)
        return context
