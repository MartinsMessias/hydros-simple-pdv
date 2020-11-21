from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from clientes.entities import cliente_entity
from clientes.forms import ClienteForm
from clientes.models import Cliente
from clientes.services import cliente_services


class ListarClientes(ListView):
    model = Cliente
    template_name = 'clientes/listar_clientes.html'

    def get(self, request, *args, **kwargs):
        context = {'clientes': cliente_services.listar_clientes() }
        return render(request, self.template_name, context)

class CadastrarCliente(ListView):
    template_name = 'clientes/form_cliente.html'

    def get(self, request, *args, **kwargs):
        form_cliente = ClienteForm()
        return render(request, self.template_name, {'form_cliente': form_cliente})

    def post(self, request, *args, **kwargs):
        form_cliente = ClienteForm(request.POST)

        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            cpf_cnpj = form_cliente.cleaned_data['cpf_cnpj']

            cliente_novo = cliente_entity.Cliente(nome=nome, cpf_cnpj=cpf_cnpj)
            cliente_services.cadastrar_cliente(cliente_novo)
            return redirect('cliente_list')
        else:
            form_cliente = ClienteForm()

        return render(request, self.template_name, {'form_cliente': form_cliente})
