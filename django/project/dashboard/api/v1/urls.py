from rest_framework.routers import DefaultRouter
from .views import SesionesViewSet

router = DefaultRouter()
router.register(r'sesiones', SesionesViewSet, basename='sesiones')

urlpatterns = router.urls
