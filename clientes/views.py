from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clientes.forms import ClienteForm
from clientes.models import Cliente

class ListarClientesView(ListView):
    model = Cliente
    template_name = 'clientes/listar_clientes.html'

class CadastrarClienteView(CreateView):
    model = Cliente
    template_name = 'clientes/form_cliente.html'
    form_class = ClienteForm
    success_url = '/clientes/'

class EditarClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'
    success_url = '/clientes/'

class RemoverClienteView(DeleteView):
    model = Cliente
    success_url = '/clientes/'