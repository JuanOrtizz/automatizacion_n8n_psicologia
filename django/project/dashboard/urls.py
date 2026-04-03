from django.urls import path
from . import views

urlpatterns= [
    path('', views.dashboard, name='dashboard'),
    path('register_sesion/', views.registrar_sesion, name='register_sesion'),
]