from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade_estoque = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} (Estoque: {self.quantidade_estoque})"


class EmprestimoEPI(models.Model):
    STATUS_CHOICES = [
        ('Emprestado', 'Emprestado'),
        ('Fornecido', 'Fornecido'),
        ('Devolvido', 'Devolvido'),
        ('Danificado', 'Danificado'),
        ('Perdido', 'Perdido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    
    data_emprestimo = models.DateField(default=timezone.now)
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Emprestado')
    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.equipamento.nome} ({self.status})"