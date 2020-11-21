from django.urls import path

from clientes.views import ListarClientes, CadastrarCliente

urlpatterns = [
    path('', ListarClientes.as_view(), name='cliente_list'),
    path('cadastrar/', CadastrarCliente.as_view(), name='cadastrar_cliente'),
]
