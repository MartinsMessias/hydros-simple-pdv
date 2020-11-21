from django.urls import path

from clientes.views import ListarClientesView, CadastrarClienteView, EditarClienteView, RemoverClienteView

urlpatterns = [
    path('', ListarClientesView.as_view(), name='listar_clientes'),
    path('cadastrar/', CadastrarClienteView.as_view(), name='cadastrar_cliente'),
    path('editar/<str:pk>', EditarClienteView.as_view(), name='editar_cliente'),
    path('remover/<str:pk>', RemoverClienteView.as_view(), name='remover_cliente'),
]
