from .views import MatchApiView, UserApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'matches', MatchApiView)
router.register(r'users', UserApiView)

urlpatterns = router.urls
