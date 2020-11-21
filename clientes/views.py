from django.shortcuts import render
from django.views import View

from clientes.models import Cliente
from clientes.services import cliente_services


class Clientes(View):
    model = Cliente
    template_name = ''

    def get(self, request, *args, **kwargs):
        context = {'clientes': cliente_services.listar_clientes() }
        return render(request, self.template_name, context)

