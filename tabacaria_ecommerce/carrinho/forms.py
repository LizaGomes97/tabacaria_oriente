from django import forms

ESCOLHAS_QUANTIDADE = [(i, str(i)) for i in range(1, 21)]

class CarrinhoAddProdutoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        choices=ESCOLHAS_QUANTIDADE,
        coerce=int,
        label='Quantidade'
    )
    substituir = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )