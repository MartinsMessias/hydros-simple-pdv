from django.urls import path

from vendas.views import *

urlpatterns = [
    path('', ListarVendasView.as_view(), name='listar_vendas'),
    path('detalhes/<str:pk>', DetalheVendaView.as_view(), name='detalhe_venda'),
    path('venda/', venda, name='venda'),
]
