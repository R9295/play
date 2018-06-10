from django.conf.urls import url
from .views import ProfileView
urlpatterns = [
    url('', ProfileView.as_view())
]
