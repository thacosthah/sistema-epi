from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"

class Equipamento(models.Model):
    nome = models.CharField(max_length=150)
    ca = models.CharField(max_length=50, verbose_name="CA (Certificado de Aprovação)")
    descricao = models.TextField(blank=True, null=True)
    quantidade_estoque = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} (CA: {self.ca})"

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
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Emprestado')
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipamento.nome} para {self.colaborador.nome} ({self.status})"