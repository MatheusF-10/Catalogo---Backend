from rest_framework import viewsets
from catalogo.models import Aula, Modulo, Usuario
from catalogo.serializer import AulaSerializer, ModuloSerializer, UsuarioSerializer


class ModulosViewSet(viewsets.ModelViewSet):
    # Abaixo funciona como se fosse uma query sql, conseguindo criar vários filtros
    queryset = Modulo.objects.all()

    # Qual a classe serializadora responsavel pelos "querys"
    serializer_class = ModuloSerializer


class AulasViewSet(viewsets.ModelViewSet):
    # Abaixo funciona como se fosse uma query sql, conseguindo criar vários filtros
    queryset = Aula.objects.all()

    # Qual a classe serializadora responsavel pelos "querys"
    serializer_class = AulaSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    # Abaixo funciona como se fosse uma query sql, conseguindo criar vários filtros
    queryset = Usuario.objects.all()

    # Qual a classe serializadora responsavel pelos "querys"
    serializer_class = UsuarioSerializer
