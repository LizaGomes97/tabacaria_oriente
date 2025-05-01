from django import forms
from .models import Pedido

class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'email', 'endereco', 'cidade', 'estado', 'cep', 'observacoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'