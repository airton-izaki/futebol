import gzip
import json
import ssl
import urllib.request
import urllib.error

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Estado, Cidade
from .serializers import EstadoSerializer, CidadeSerializer, CidadeIBGESerializer


class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estado.objects.all().order_by('nome_estado')
    serializer_class = EstadoSerializer


class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CidadeSerializer

    def get_queryset(self):
        qs = Cidade.objects.select_related('estado').order_by('nome_cidade')
        estado = self.request.query_params.get('estado')
        search = self.request.query_params.get('search')
        if estado:
            qs = qs.filter(estado__codigo_ibge=estado)
        if search:
            qs = qs.filter(nome_cidade__icontains=search)
        return qs[:50]


class CidadesIBGEView(APIView):
    """
    Busca municípios diretamente na API pública do IBGE.
    Parâmetros:
        estado  — código IBGE do estado (obrigatório)
        search  — filtro parcial pelo nome da cidade (opcional)
    """

    IBGE_URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios?orderBy=nome'

    def get(self, request):
        estado_id = request.query_params.get('estado', '').strip()
        search    = request.query_params.get('search', '').strip().lower()

        if not estado_id:
            return Response(
                {'erro': 'Parâmetro "estado" é obrigatório.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        url = self.IBGE_URL.format(estado=estado_id)
        req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
        try:
            ctx = ssl.create_default_context()
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                raw = resp.read()
                if resp.info().get('Content-Encoding') == 'gzip':
                    raw = gzip.decompress(raw)
                municipios = json.loads(raw)
        except urllib.error.URLError as exc:
            return Response(
                {'erro': f'Falha ao consultar a API do IBGE: {exc}'},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        cidades = [{'codigo_ibge': m['id'], 'nome': m['nome']} for m in municipios]

        if search:
            cidades = [c for c in cidades if search in c['nome'].lower()]

        serializer = CidadeIBGESerializer(cidades, many=True)
        return Response(serializer.data)
