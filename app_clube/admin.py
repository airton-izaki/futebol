from django.contrib import admin
from .models import Clube


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display    = ('nome_clube', 'nome', 'sigla', 'cidade', 'estado', 'fundacao', 'ativo')
    list_filter     = ('estado', 'ativo')
    search_fields   = ('nome', 'nome_clube', 'sigla', 'cidade')
    ordering        = ('nome',)
