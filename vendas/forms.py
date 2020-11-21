from django import forms

from clientes.models import Cliente
from vendas.models import ItemVendaDetalhes, Venda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(VendaForm, self).__init__(*args, **kwargs)

class ItemForm(forms.ModelForm):

    class Meta:
        model = ItemVendaDetalhes
        fields = ('venda', )

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(AddItemForm, self).__init__(*args, **kwargs)