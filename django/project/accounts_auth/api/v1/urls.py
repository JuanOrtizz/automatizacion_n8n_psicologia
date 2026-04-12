from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.throttling import ScopedRateThrottle
from django.urls import path
from .views import UserViewSet
from project.throttles import LoginAnonRateThrottle

class ThrottledTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [ScopedRateThrottle, LoginAnonRateThrottle]

class ThrottledTokenRefreshView(TokenRefreshView):
    throttle_classes = [ScopedRateThrottle, LoginAnonRateThrottle]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='accounts_auth')

urlpatterns = [
    path('token/', ThrottledTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', ThrottledTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls