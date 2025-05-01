from django import forms
from .models import Tecido, Aviamento

class TecidoForm(forms.ModelForm):
    class Meta:
        model = Tecido
        fields = ['artigo', 'cor', 'fornecedor', 'cliente', 'metragem']

class AviamentoForm(forms.ModelForm):
    class Meta:
        model = Aviamento
        fields = ['artigo', 'cor', 'fornecedor', 'cliente', 'quantidade']

