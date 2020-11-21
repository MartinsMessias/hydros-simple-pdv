from django.db import models
from django.utils import timezone

from clientes.models import Cliente
from produtos.models import Produto


class Venda(models.Model):
    FORMAS_DE_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    forma_pagamento = models.CharField(choices=FORMAS_DE_PAGAMENTO, max_length=8)
    valor_total = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.data} - {self.cliente.nome}'


class ItemVendaDetalhes(models.Model):
    venda_id = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)


    def __str__(self):
        return f'{self.produto.produto} - {self.produto.valor}'