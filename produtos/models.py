from django.core.validators import MinValueValidator
from django.db import models

class Produto(models.Model):
    produto = models.CharField(max_length=256)
    codigo = models.CharField(max_length=13, unique=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.produto} - R$ {self.valor}'