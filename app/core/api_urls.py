from rest_framework import routers

from . import api_views as api

app_name = 'core-api'

router = routers.DefaultRouter()
router.register(r'usuarios', api.UUIDUserViewSet, base_name='api-users')

urlpatterns = router.urls