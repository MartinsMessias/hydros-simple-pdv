from django.views.generic import ListView, CreateView
from clientes.forms import ClienteForm
from clientes.models import Cliente

class ListarClientesView(ListView):
    model = Cliente
    template_name = 'clientes/listar_clientes.html'

class CadastrarCliente(CreateView):
    model = Cliente
    template_name = 'clientes/form_cliente.html'
    form_class = ClienteForm
    success_url = '/clientes/listar/'
