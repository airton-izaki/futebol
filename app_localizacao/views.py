from rest_framework.decorators import api_view
from rest_framework.response   import Response
from .models                   import Cidade


@api_view(['GET'])
def cidades_por_uf(request):
    """
    GET /api/cidades/?uf=SP&q=cam
    Retorna cidades filtradas por UF e opcionalmente por nome (mínimo 2 chars).
    """
    uf = request.query_params.get('uf', '').upper().strip()
    q  = request.query_params.get('q',  '').strip()

    if not uf:
        return Response({'erro': 'Parâmetro "uf" obrigatório.'}, status=400)

    qs = Cidade.objects.filter(estado__uf=uf).order_by('nome_cidade')

    if len(q) >= 2:
        qs = qs.filter(nome_cidade__icontains=q)

    cidades = list(qs.values_list('nome_cidade', flat=True)[:50])
    return Response(cidades)
