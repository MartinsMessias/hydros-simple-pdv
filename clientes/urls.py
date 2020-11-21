from django.urls import path

from clientes.views import ListarClientesView, CadastrarCliente

urlpatterns = [
    path('listar/', ListarClientesView.as_view(), name='listar_clientes'),
    path('cadastrar/', CadastrarCliente.as_view(), name='cadastrar_cliente'),
]
