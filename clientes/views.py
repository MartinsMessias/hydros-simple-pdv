from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from clientes.forms import ClienteForm
from clientes.models import Cliente

class ListarClientesView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/listar_clientes.html'
    paginate_by = 6

class CadastrarClienteView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'clientes/form_cliente.html'
    form_class = ClienteForm
    success_url = '/clientes/'

class EditarClienteView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'
    success_url = '/clientes/'

class RemoverClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = '/clientes/'

class DetalhesClienteView(LoginRequiredMixin, DetailView):
    model = Cliente
