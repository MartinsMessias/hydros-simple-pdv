from django.http import Http404

from ..models import Venda

def listar_vendas():
    vendas = Venda.objects.all()
    return vendas

def cadastrar_venda(venda):
    return Venda.objects.create(venda)

def listar_venda_por_id(id):
    try:
        return Venda.objects.get(id)
    except Venda.DoesNotExist:
        raise Http404

# def editar_venda(venda, novos_dados_venda):
#     pass

def remover_venda(venda):
    venda.delete()
