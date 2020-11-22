from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from vendas.forms import VendaForm, VendaItemForm
from vendas.models import Venda, VendaItem

def venda(request):
    venda_forms_data = Venda()
    item_venda_formset = inlineformset_factory(
        Venda, VendaItem, form=VendaItemForm,
        extra=0, can_delete=False, min_num=1, validate_min=True,)

    if request.method == 'POST':
        forms = VendaForm(request.POST, instance=venda_forms_data, prefix='main')
        formset = item_venda_formset(request.POST, instance=venda_forms_data, prefix='product')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return redirect('listar_vendas')
    else:
        forms = VendaForm(instance=venda_forms_data, prefix='main')
        formset = item_venda_formset(instance=venda_forms_data, prefix='product')

    context = {
        'form': forms,
        'formset': formset,
    }
    return render(request, 'vendas/form_venda.html', context)

class ListarVendasView(ListView):
    model = Venda
    template_name = 'vendas/listar_vendas.html'
    ordering = ['-id']

class DetalheVendaView(DetailView):
    model = VendaItem
    template_name = 'vendas/venda_detail.html'

