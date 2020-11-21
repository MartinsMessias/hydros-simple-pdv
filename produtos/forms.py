from django import forms

from produtos.models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Coloca em todos os campos que não tem uma 'class' do CSS, um 'form-control'.
        for l in self.base_fields:
            if not self.base_fields[l].widget.attrs.get('class'):
                self.base_fields[l].widget.attrs['class'] = 'form-control'

        super(ProdutoForm, self).__init__(*args, **kwargs)