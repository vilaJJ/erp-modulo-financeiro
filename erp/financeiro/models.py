from django.db import models

# Create your models here.

class ContaPagar(models.Model):
    codigo_fornecedor = models.IntegerField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("pendente", "Pendente"), ("paga", "Paga")],
        default="pendente"
    )

    def __str__(self):
        return self.descricao

class ContaReceber(models.Model):
    codigo_cliente = models.IntegerField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_prevista = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("pendente", "Pendente"), ("recebida", "Recebida")],
        default="pendente"
    )

    def __str__(self):
        return self.descricao