from django import forms

from vendas.models import Venda, VendaItem


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        exclude = ['usuario', ]

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(VendaForm, self).__init__(*args, **kwargs)


class VendaItemForm(forms.ModelForm):

    class Meta:
        model = VendaItem
        exclude = ['venda', ]

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(VendaItemForm, self).__init__(*args, **kwargs)