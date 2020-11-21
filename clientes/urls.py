from django.urls import path

from clientes.views import ListarClientesView, CadastrarClienteView, EditarClienteView, RemoverClienteView, DetalhesClienteView

urlpatterns = [
    path('', ListarClientesView.as_view(), name='listar_clientes'),
    path('detalhes/<str:pk>', DetalhesClienteView.as_view(), name='detalhes_cliente'),
    path('cadastrar/', CadastrarClienteView.as_view(), name='cadastrar_cliente'),
    path('editar/<str:pk>', EditarClienteView.as_view(), name='editar_cliente'),
    path('remover/<str:pk>', RemoverClienteView.as_view(), name='remover_cliente'),
]
