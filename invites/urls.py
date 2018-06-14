from django.conf.urls import url
from .views import InviteView

urlpatterns = [
    url('', InviteView.as_view(), name='invite')
]
