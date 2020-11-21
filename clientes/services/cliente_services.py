from django.http import Http404

from ..models import Cliente

def listar_clientes():
    clientes = Cliente.objects.all()
    return clientes

def cadastrar_cliente(cliente):
    return Cliente.objects.create(cliente)

def listar_cliente_por_id(id):
    try:
        return Cliente.objects.get(id)
    except Cliente.DoesNotExist:
        raise Http404

def editar_cliente(cliente, novos_dados_cliente):
    cliente.nome = novos_dados_cliente.nome
    cliente.cpf_cnpj = novos_dados_cliente.cpf_cnpj
    cliente.save(force_update=True)

def remover_cliente(cliente):
    cliente.delete()
