from django.http import Http404

from ..models import ItemVendaDetalhes

def listar_vendas():
    vendas = ItemVendaDetalhes.objects.all()
    return vendas

def cadastrar_venda(venda):
    return ItemVendaDetalhes.objects.create(venda)

def listar_venda_por_id(id):
    try:
        return ItemVendaDetalhes.objects.get(id)
    except ItemVendaDetalhes.DoesNotExist:
        raise Http404

# def editar_venda(venda, novos_dados_venda):
#     pass

def remover_venda(venda):
    venda.delete()
