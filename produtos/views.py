from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from produtos.forms import ProdutoForm
from produtos.models import Produto

class ListarProdutosView(ListView):
    model = Produto
    template_name = 'produtos/listar_produtos.html'

class CadastrarProdutoView(CreateView):
    model = Produto
    template_name = 'produtos/form_produto.html'
    form_class = ProdutoForm
    success_url = '/produtos/'

class EditarProdutoView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form_produto.html'
    success_url = '/produtos/'

class RemoverProdutoView(DeleteView):
    model = Produto
    success_url = '/produtos/'

class DetalhesProdutoView(DetailView):
    model = Produto
