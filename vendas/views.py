from django.shortcuts import render

from django.views.generic import ListView, CreateView, FormView
from vendas.forms import VendaForm
from vendas.models import ItemVendaDetalhes, Venda


class ListarVendasView(ListView):
    model = ItemVendaDetalhes
    template_name = 'vendas/listar_vendas.html'


class VenderView(FormView):
    template_name = 'vendas/form_venda.html'
    form_class = VendaForm
    success_url = 'vendas/'

