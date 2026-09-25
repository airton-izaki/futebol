from rest_framework import serializers
import requests

from app_localizacao.models import Cidade, Estado
from .models import Clube


class ClubeSerializer(serializers.ModelSerializer):
    # The form uses these names; the existing model stores them under
    # nome / nome_clube and stores city and state as text.
    nome_clube = serializers.CharField(source='nome', max_length=100)
    nickname = serializers.CharField(source='nome_clube', max_length=100)
    data_fundacao = serializers.DateField(source='fundacao')
    cidade = serializers.CharField(read_only=True)
    estado = serializers.CharField(read_only=True)
    cidade_ibge = serializers.IntegerField(write_only=True, required=False)
    codigo_ibge = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Clube
        fields = [
            'id', 'nome_clube', 'nickname', 'sigla', 'data_fundacao', 'gestao',
            'cidade', 'estado', 'cidade_ibge', 'codigo_ibge', 'estadio',
            'cor_primaria', 'cor_secundaria', 'cor_terciaria', 'website',
            'escudo', 'descricao', 'ativo', 'criado_em', 'atualizado_em',
        ]

    def validate(self, attrs):
        codigo = attrs.pop('cidade_ibge', None) or attrs.pop('codigo_ibge', None)
        if codigo:
            cidade = Cidade.objects.select_related('estado').filter(codigo_ibge=codigo).first()
            if cidade is None:
                try:
                    resposta = requests.get(
                        f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}',
                        timeout=10,
                    )
                    resposta.raise_for_status()
                    dados = resposta.json()
                    estado_codigo = dados['microrregiao']['mesorregiao']['UF']['id']
                    estado = Estado.objects.filter(codigo_ibge=estado_codigo).first()
                    cidade = Cidade.objects.create(
                        codigo_ibge=dados['id'], nome_cidade=dados['nome'], estado=estado
                    )
                except (requests.RequestException, KeyError, TypeError, ValueError):
                    raise serializers.ValidationError({
                        'codigo_ibge': 'Não foi possível validar a cidade no IBGE.'
                    })
            attrs['cidade'] = cidade.nome_cidade
            attrs['estado'] = cidade.estado.uf if cidade.estado else ''
        return attrs
