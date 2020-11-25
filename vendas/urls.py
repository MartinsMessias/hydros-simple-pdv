from django.urls import path

from vendas.views import *

urlpatterns = [
    path('', ListarVendasView.as_view(), name='listar_vendas'),
    path('venda/', VendaView, name='venda'),
    path('detalhes/<str:pk>', DetalheVendaView.as_view(), name='detalhe_venda'),
    path('editar/<str:pk>', VendaEditarView, name='editar_venda'),
    path('relatorio/<str:id>', gerar_relatorio, name='gerar_relatorio'),
    # path('ajax_calls/search/', autocompletar),
]
