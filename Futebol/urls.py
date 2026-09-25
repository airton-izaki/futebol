"""
URL configuration for Futebol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf            import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.contrib         import admin
from django.urls            import path, include
from app_home.views         import HomeView
from app_clube.views        import ClubeViewSet, ClubeCreateView, ClubeListView, ClubeUpdateView
from app_localizacao.views  import EstadoViewSet, CidadeViewSet, CidadesIBGEView

router = DefaultRouter()
router.register(r'clubes',   ClubeViewSet,  basename ='clube')
router.register(r'estados',  EstadoViewSet, basename ='estado')
router.register(r'cidades',  CidadeViewSet, basename ='cidade')




urlpatterns = [
    path('',                    HomeView.as_view(),         name ='index'),

    path('clube/cadastrar',     ClubeCreateView.as_view(),  name ='criar_clube'),
    path('clube/',              ClubeListView.as_view(),    name ='clube'),
    path('editar/<int:pk>/',    ClubeUpdateView.as_view(),  name ='editar_clube'),

    path('api/cidades-ibge/',   CidadesIBGEView.as_view(),  name ='cidades_ibge'),

    path('api/',  include(router.urls)),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
