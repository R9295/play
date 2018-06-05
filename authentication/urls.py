from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from authentication.views import LoginView, LogoutView

urlpatterns = [
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^logout', login_required(LogoutView.as_view(), login_url='/login'), name='logout')
]
