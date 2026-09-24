from django.contrib import admin
from .models import Clube


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display    = ('nome', 'sigla', 'cidade', 'estado', 'divisao', 'fundacao', 'ativo')
    list_filter     = ('divisao', 'estado', 'ativo')
    search_fields   = ('nome', 'sigla', 'cidade')
    ordering        = ('nome',)
