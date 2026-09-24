from rest_framework     import serializers
from .models            import Estado, Cidade


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['codigo_ibge', 'uf', 'nome_estado', 'regiao_estado']

class CidadeSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only = True)

    class Meta:
        model = Cidade
        fields = ['codigo_ibge', 'nome_cidade', 'estado', 'pais']



