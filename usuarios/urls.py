from django.urls import path

from produtos.views import *
from usuarios.views import CadastrarUsuarioView

urlpatterns = [
    # path('', ListarProdutosView.as_view(), name='listar_produtos'),
    # path('detalhes/<str:pk>', DetalhesProdutoView.as_view(), name='detalhes_produto'),
    path('cadastrar/', CadastrarUsuarioView.as_view(), name='cadastrar_usuario'),
    # path('editar/<str:pk>', EditarProdutoView.as_view(), name='editar_produto'),
    # path('remover/<str:pk>', RemoverProdutoView.as_view(), name='remover_produto'),
]
