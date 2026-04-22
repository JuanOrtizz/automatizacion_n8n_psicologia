from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.throttling import ScopedRateThrottle
from drf_spectacular.utils import extend_schema
from django.urls import path
from .views import UserViewSet
from project.throttles import LoginAnonRateThrottle

class ThrottledTokenObtainPairView(TokenObtainPairView):
    throttle_schema = None
    @extend_schema(summary="Obtener token", description="Obtiene tokens JWT con username y password")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ThrottledTokenRefreshView(TokenRefreshView):
    @extend_schema(summary="Refrescar token", description="Refresca el token de acceso usando el refresh token")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='accounts_auth')

urlpatterns = [
    path('token/', ThrottledTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', ThrottledTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls