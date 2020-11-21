from django.db import models
from django.utils import timezone

from clientes.models import Cliente
from produtos.models import Produto


class ItemVendaDetalhes(models.Model):
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.produto.produto


class Venda(models.Model):

    FORMAS_DE_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    forma_pagamento = models.CharField(choices=FORMAS_DE_PAGAMENTO, max_length=8)
    valor_total = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.cliente.nome

