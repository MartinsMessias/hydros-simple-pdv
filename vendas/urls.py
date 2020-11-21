from django.urls import path

from vendas.views import *

urlpatterns = [
    path('', ListarVendasView.as_view(), name='listar_vendas'),
    # path('detalhes/<str:pk>', DetalhesProdutoView.as_view(), name='detalhes_produto'),
    # path('cadastrar/', CadastrarProdutoView.as_view(), name='cadastrar_produto'),
    # path('editar/<str:pk>', EditarProdutoView.as_view(), name='editar_produto'),
    # path('remover/<str:pk>', RemoverProdutoView.as_view(), name='remover_produto'),
]
