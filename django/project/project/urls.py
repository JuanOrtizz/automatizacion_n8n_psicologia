from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts_auth/', include('accounts_auth.urls')),
    path('', include('dashboard.urls')),
]
