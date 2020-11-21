from django.urls import path

from clientes.views import Clientes

urlpatterns = [
    path('', Clientes.as_view(), name='clientes'),
]
