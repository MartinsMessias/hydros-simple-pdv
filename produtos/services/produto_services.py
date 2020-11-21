from django.http import Http404

from ..models import Produto

def listar_produtos():
    produtos = Produto.objects.all()
    return produtos

def cadastrar_produto(produto):
    return Produto.objects.create(produto)

def listar_produto_por_codigo(codigo):
    try:
        return Produto.objects.get(codigo__exact=codigo)
    except Produto.DoesNotExist:
        raise Http404

def editar_produto(produto, novos_dados_produto):
    produto.produto = novos_dados_produto.produto
    produto.codigo = novos_dados_produto.codigo
    produto.valor = novos_dados_produto.valor
    produto.descricao = novos_dados_produto.descricao
    produto.quantidade = novos_dados_produto.quantidade
    produto.save(force_update=True)

def remover_produto(produto):
    produto.delete()
