from django.contrib import admin
from django.urls import path, include
from catalogo.views import ModulosViewSet, AulasViewSet, UsuariosViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'modulos', ModulosViewSet)
router.register(r'aulas', AulasViewSet)
router.register(r'usuarios', UsuariosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
