from django.urls import path

from vendas.views import *

urlpatterns = [
    path('', ListarVendasView.as_view(), name='listar_vendas'),
]