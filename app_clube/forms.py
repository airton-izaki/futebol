from django import forms
from .models import Clube


class ClubeForm(forms.ModelForm):

    class Meta:
        model  = Clube
        fields = [
            'nome', 'sigla', 'fundacao', 'cidade', 'estado',
            'estadio', 'divisao',
            'cor_primaria', 'cor_secundaria',
            'website',
            'escudo', 'descricao', 'ativo',
        ]
        widgets = {
            'nome':           forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sport Club Corinthians Paulista'}),
            'sigla':          forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: SCCP', 'maxlength': '5'}),
            'fundacao':       forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cidade':         forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: São Paulo'}),
            'estado':         forms.Select(attrs={'class': 'form-select'}),
            'estadio':        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Neo Química Arena'}),
            'divisao':        forms.Select(attrs={'class': 'form-select'}),
            'cor_primaria':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Preto'}),
            'cor_secundaria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Branco'}),
            'website':        forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ex: https://www.clube.com.br'}),
            'escudo':         forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descricao':      forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Breve história ou informações sobre o clube...'}),
            'ativo':          forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
