from rest_framework                     import viewsets
from django.views.generic               import CreateView, ListView, UpdateView
from django.urls                        import reverse_lazy
from app_clube.models                   import Clube
from app_clube.serializers              import ClubeSerializer
from app_clube.forms.clubecreateform    import ClubeForm
from app_localizacao.models             import Cidade, Estado



class ClubeViewSet(viewsets.ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer

class ClubeCreateView(CreateView):
    model = Clube
    template_name = 'app_clube/createclube.html'
    form_class = ClubeForm
    success_url = reverse_lazy('clube')

class ClubeListView(ListView):
    model = Clube
    template_name = 'app_clube/clube.html'
    context_object_name = 'clubes'

    def get_queryset(self):
        return Clube.objects.filter(ativo = True)

class ClubeUpdateView(UpdateView):
    model = Clube
    form_class = ClubeForm
    template_name = 'app_clube/createclube.html'
    success_url = reverse_lazy('clube')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estado = Estado.objects.filter(uf=self.object.estado).first()
        cidade = Cidade.objects.filter(
            nome_cidade=self.object.cidade,
            estado__uf=self.object.estado,
        ).first()
        context['estado_atual_codigo'] = estado.codigo_ibge if estado else ''
        context['cidade_atual_codigo'] = cidade.codigo_ibge if cidade else ''
        return context
