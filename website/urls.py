from django.urls import path  # Erro 1: Corrigido de 'rom' para 'from'
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipe/', views.equipe, name='equipe'),
    path('sobre/', views.sobre, name='sobre'),
]