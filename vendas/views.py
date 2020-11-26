import json
import tempfile

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView

from weasyprint import HTML

from vendas.forms import VendaForm, VendaItemForm, ItemVendaFormSet
from vendas.models import Venda, VendaItem


class VendaView(LoginRequiredMixin, CreateView):
    template_name = 'vendas/form_venda.html'
    form_class = VendaForm

    def get_context_data(self, **kwargs):
        context = super(VendaView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['forms'] = VendaForm(self.request.POST)
            context['formset'] = ItemVendaFormSet(self.request.POST)
        else:
            context['forms'] = VendaForm()
            context['formset'] = ItemVendaFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forms = context['forms']
        formset = context['formset']

        if forms.is_valid() and formset.is_valid():
            self.object = form.save()
            forms.instance = self.object
            formset.instance = self.object
            forms.save()
            formset.save()

            venda_realizada = Venda.objects.latest('id')
            context = {"object": venda_realizada}
            return render(self.request, 'vendas/venda_detail.html', context)
        else:
            return self.render_to_response(self.get_context_data(form=form))


# def VendaEditarView(request, pk):
#     if request.method == "GET":
#         venda = VendaItem.objects.get(pk=pk)
#
#         if not venda:
#             return redirect('listar_vendas')
#
#         form_venda = VendaForm(instance=venda)
#         form_item_factory = inlineformset_factory(Venda, VendaItem, form=VendaItemForm, extra=3)
#         form_item = form_item_factory(instance=venda)
#
#         context = {
#             'form_venda': form_venda,
#             'form_item': form_item,
#         }
#         return render(request,'vendas/form_venda.html', context)
#
#     elif request.method == "POST":
#         venda = Venda.objects.get(pk=pk)
#
#         if not venda:
#             return redirect('listar_vendas')
#
#         form_venda = VendaForm(request.POST, instance=venda)
#         form_item_factory = inlineformset_factory(Venda, VendaItem, form=VendaItemForm)
#         form_item = form_item_factory(request.POST, instance=venda)
#
#         if form_venda.is_valid() and form_item.is_valid():
#             venda = form_venda.save()
#             form_item.instance = venda
#             form_item.save()
#             return redirect('listar_vendas')
#         else:
#             context = {
#                 'form_venda': form_venda,
#                 'form_item': form_item
#             }
#             return render(request, 'vendas/form_venda.html', context)

class ListarVendasView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'vendas/listar_vendas.html'
    ordering = ['-id']
    paginate_by = 6


class DetalheVendaView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'vendas/venda_detail.html'

# @login_required
# def autocompletar(request):
#     if request.is_ajax():
#         produto = request.GET.get('term', '')
#         produtos = Produto.objects.filter(produto__startswith=produto)
#
#         results = []
#
#         for produto in produtos:
#             results.append(str(f'{produto.produto} - R$ {produto.valor}'))
#
#         data = json.dumps(results)
#     else:
#         data = ''
#
#     return HttpResponse(data, 'application/json')

@login_required
def gerar_relatorio(request, id):
    #Traz os dados do ORM
    venda = Venda.objects.get(id=id)

    #Junta-se o template com os dados e salvamos em uma string
    html_string = render_to_string('vendas/venda_detail_pdf.html', {'dados': venda})

    #Tranformamos em HTML
    html = HTML(string=html_string)

    #Transforma o html em um PDF
    resultado_pdf = html.write_pdf()

    #Tratamento da resposta para o navegador entender de que se trata de um arquivo pdf
    resposta = HttpResponse(content_type='application/pdf;')
    resposta['Content-Disposition'] = 'inline; filename=relatorio.pdf'
    resposta['Content-Transfer-Encoding'] = 'binary'

    # Cria-se um arquivo temporario para o usuário realizar o download
    with tempfile.NamedTemporaryFile(delete=True) as output:
        # Os dados irão ser copiados para esse arquivo temp..
        output.write(resultado_pdf)
        output.flush()
        output = open(output.name, 'rb')
        resposta.write(output.read())

    # Retorne para o usuario o arquivo temporário
    return resposta