from .views import MatchApiView, UserApiView, ServerApiView, RoleApiView, HeroApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'matches', MatchApiView)
router.register(r'users', UserApiView)
router.register(r'heroes', HeroApiView)
router.register(r'roles', RoleApiView)
router.register(r'servers', ServerApiView)

urlpatterns = router.urls
