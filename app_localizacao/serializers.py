from rest_framework     import serializers
from .models            import Estado, Cidade


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['codigo_ibge', 'uf', 'nome_estado', 'regiao_estado']


class CidadeSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='nome_cidade', read_only=True)
    estado = EstadoSerializer(read_only=True)

    class Meta:
        model = Cidade
        fields = ['codigo_ibge', 'nome', 'estado', 'pais']


class CidadeIBGESerializer(serializers.Serializer):
    """Serializa municípios retornados diretamente pela API do IBGE."""
    codigo_ibge = serializers.IntegerField()
    nome        = serializers.CharField()


