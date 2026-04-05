from django.urls import path
from . import views

urlpatterns= [
    path('', views.dashboard, name='dashboard'),
    path('registrar-sesion/', views.registrar_sesion, name='registrar-sesion'),
    path('modificar-sesion/<int:sesion_id>/', views.modificar_sesion, name='modificar-sesion'),
    path('eliminar-sesion/<int:sesion_id>/', views.eliminar_sesion, name='eliminar-sesion'),
]