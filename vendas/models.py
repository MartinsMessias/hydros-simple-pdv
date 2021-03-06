from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField # Campo do Usuário atual

from clientes.models import Cliente
from produtos.models import Produto

class VendaItem(models.Model):
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True, default='produto')
    quantidade = models.PositiveIntegerField(default=1)
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.venda.id} - {self.produto.quantidade}'


class Venda(models.Model):

    FORMAS_DE_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
    )
    usuario = CurrentUserField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    forma_pagamento = models.CharField(choices=FORMAS_DE_PAGAMENTO, max_length=8)
    valor_total = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return f'ID VENDA: {self.id}'
