from django.contrib import admin
from catalogo.models import Aula, Modulo, Usuario


class Aulas(admin.ModelAdmin):
    # Campos que eu quero mostrar!
    list_display = ('id', 'nome', 'fk_modulo')

    # Campos que vou conseguir clicar para manipular os dados das informações
    list_display_links = ('id', 'nome')

    # Campos que vou conseguir buscar
    search_fields = ('nome',)


class Modulos(admin.ModelAdmin):
    # Campos que eu quero mostrar!
    list_display = ('id', 'nome')

    # Campos que vou conseguir clicar para manipular os dados das informações
    list_display_links = ('id', 'nome')

    # Campos que vou conseguir buscar
    search_fields = ('nome',)


class Usuarios(admin.ModelAdmin):
    # Campos que eu quero mostrar!
    list_display = ('id', 'nome', 'rg')

    # Campos que vou conseguir clicar para manipular os dados das informações
    list_display_links = ('id', 'nome')

    # Campos que vou conseguir buscar
    search_fields = ('nome',)


# Disponibilizo para conseguir visualizar no admin do django
admin.site.register(Aula, Aulas)
admin.site.register(Modulo, Modulos)
admin.site.register(Usuario, Usuarios)
