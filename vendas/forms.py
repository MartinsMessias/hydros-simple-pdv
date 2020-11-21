from django import forms

from vendas.models import ItemVendaDetalhes


class VendaForm(forms.ModelForm):

    class Meta:
        model = ItemVendaDetalhes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(VendaForm, self).__init__(*args, **kwargs)