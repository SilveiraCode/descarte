from django import forms
from .models import SolicitacaoColeta

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoColeta
        fields = ['categoria', 'descricao', 'cep', 'bairro', 'rua', 'endereco_numero', 'foto']
        widgets = {
            'cep': forms.TextInput(attrs={
                'class': 'form-control', 
                'onblur': 'buscarEnderecoPeloCEP(this.value)', 
                'placeholder': '89245-000',
                'id': 'id_cep'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'id_bairro',
                'placeholder': 'Bairro'
            }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'id_rua',
                'placeholder': 'Nome da rua...'
            }),
            'endereco_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
