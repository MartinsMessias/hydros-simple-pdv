from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from clientes.models import Cliente
from produtos.models import Produto
from vendas.models import Venda


class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):

        produtos_totais = Produto.objects.all().count()
        clientes_totais = Cliente.objects.all().count()
        vendas_totais = Venda.objects.all().count()
        receita_total = Venda.objects.all().aggregate(valor_total=Sum('valor_total')).get('valor_total')

        context = {
            'produtos_total': produtos_totais,
            'clientes_total': clientes_totais,
            'vendas_total': vendas_totais,
            'receita_total': receita_total
        }
        return render(request, self.template_name, context)