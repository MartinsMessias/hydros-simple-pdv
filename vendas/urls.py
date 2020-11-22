from django.conf.urls import url
from django.urls import path

from vendas.views import *

urlpatterns = [
    path('', ListarVendasView.as_view(), name='listar_vendas'),
    path('detalhes/<str:pk>', DetalheVendaView.as_view(), name='detalhe_venda'),
    path('venda/', venda, name='venda'),
    path('relatorio/', gerar_relatorio, name='gerar_relatorio'),
    path('ajax_calls/search/', autocompletar),
]
