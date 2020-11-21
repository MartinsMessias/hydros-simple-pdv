from django import forms

from clientes.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(ClienteForm, self).__init__(*args, **kwargs)