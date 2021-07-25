from rest_framework import serializers
from catalogo.models import Aula, Modulo, Usuario


# Abaixo, eu configuro que será um serializador relacionado a um modelo
class ModuloSerializer(serializers.ModelSerializer):
    # Abaixo eu indico qual o modelo que irei indicar e quais os campos, seguindo a doc do rest_framework
    class Meta:
        model = Modulo
        fields = ['id', 'nome', 'num_aulas']

# Abaixo, eu configuro que será um serializador relacionado a um modelo


class AulaSerializer(serializers.ModelSerializer):
    # Abaixo eu indico qual o modelo que irei indicar e quais os campos, seguindo a doc do rest_framework
    class Meta:
        model = Aula
        fields = ['id', 'nome', 'fk_modulo', 'data_aula']

# Abaixo, eu configuro que será um serializador relacionado a um modelo


class UsuarioSerializer(serializers.ModelSerializer):
    # Abaixo eu indico qual o modelo que irei indicar e quais os campos, seguindo a doc do rest_framework
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'rg', 'tipo', ]
