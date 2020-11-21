from django import forms

from clientes.models import Cliente


class ClienteForm(forms.Form):

    class Meta:
        model = Cliente
        fields = '__all__'