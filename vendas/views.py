from django.shortcuts import render

from django.views.generic import ListView
from vendas.forms import VendaForm
from vendas.models import ItemVendaDetalhes

class ListarVendasView(ListView):
    model = ItemVendaDetalhes
    template_name = 'vendas/listar_vendas.html'
