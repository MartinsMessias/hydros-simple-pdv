from django.shortcuts import render, redirect
from django.views import View

from clientes.entities import cliente_entity
from clientes.forms import ClienteForm
from clientes.models import Cliente
from clientes.services import cliente_services


class Clientes(View):
    model = Cliente

    def get(self, request, *args, **kwargs):
        context = {'clientes': cliente_services.listar_clientes() }
        return render(request, 'clientes/listar_clientes.html', context)


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

        return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente})
