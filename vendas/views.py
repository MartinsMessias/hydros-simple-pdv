from django.views.generic import ListView

from vendas.models import ItemVendaDetalhes


class ListarVendasView(ListView):
    model = ItemVendaDetalhes
    template_name = 'vendas/listar_vendas.html'


