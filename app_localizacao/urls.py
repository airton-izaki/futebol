from django.urls import path
from .views import cidades_por_uf

urlpatterns = [
    path('cidades/', cidades_por_uf, name='api-cidades'),
]
