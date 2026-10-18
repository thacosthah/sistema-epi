from django import forms
from .models import Colaborador, Equipamento, EmprestimoEPI

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'cargo', 'setor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'ca', 'descricao', 'quantidade_estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ca': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmprestimoEPIForm(forms.ModelForm):
    class Meta:
        model = EmprestimoEPI
        fields = ['colaborador', 'equipamento', 'data_prevista_devolucao', 'status', 'observacao']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'equipamento': forms.Select(attrs={'class': 'form-control'}),
            'data_prevista_devolucao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }