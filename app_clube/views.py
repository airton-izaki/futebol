from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Clube
from .forms import ClubeForm


class Campeonato_Futebol(CreateView):
    model         = Clube
    form_class    = ClubeForm
    template_name = 'app_clube/clube.html'
    success_url   = reverse_lazy('clube')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubes'] = Clube.objects.all()
        return context
