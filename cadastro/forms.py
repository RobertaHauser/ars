from django import forms
from .models import Unidade

class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = ['sigla', 'nome']
        #fiels="__all__"