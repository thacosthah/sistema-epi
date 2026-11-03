from django import forms
from .models import Colaborador, Equipamento, EmprestimoEPI

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'cargo', 'setor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
            'setor': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
        }

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'quantidade_estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control bg-secondary text-light border-0', 'rows': 3}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
        }

class EmprestimoEPIForm(forms.ModelForm):
    class Meta:
        model = EmprestimoEPI
        fields = ['colaborador', 'equipamento', 'quantidade', 'data_emprestimo', 'data_prevista_devolucao', 'status', 'data_devolucao', 'observacao_devolucao']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
            'equipamento': forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control bg-secondary text-light border-0'}),
            'data_emprestimo': forms.DateInput(attrs={'class': 'form-control bg-secondary text-light border-0', 'type': 'date'}),
            'data_prevista_devolucao': forms.DateInput(attrs={'class': 'form-control bg-secondary text-light border-0', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select bg-secondary text-light border-0'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control bg-secondary text-light border-0', 'type': 'date'}),
            'observacao_devolucao': forms.Textarea(attrs={'class': 'form-control bg-secondary text-light border-0', 'rows': 2}),
        }