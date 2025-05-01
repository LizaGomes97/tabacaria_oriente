from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ItemPedido, Pedido
from .forms import PedidoCreateForm
from carrinho.cart import Carrinho

def checkout(request):
    carrinho = Carrinho(request)
    
    if len(carrinho) == 0:
        messages.warning(request, 'Seu carrinho está vazio!')
        return redirect('produtos:lista_produtos')
        
    if request.method == 'POST':
        form = PedidoCreateForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            if request.user.is_authenticated:
                pedido.usuario = request.user
            pedido.save()
            
            for item in carrinho:
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item['produto'],
                    preco=item['preco'],
                    quantidade=item['quantidade']
                )
            
            # Limpar o carrinho
            carrinho.limpar()
            
            return render(request, 'pedidos/confirmacao.html', {'pedido': pedido})
    else:
        # Pré-preencher dados do usuário autenticado
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'nome': request.user.get_full_name(),
                'email': request.user.email,
            }
        form = PedidoCreateForm(initial=initial_data)
    
    return render(request, 'pedidos/checkout.html', {
        'form': form,
        'carrinho': carrinho
    })

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})

@login_required
def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'pedidos/detalhe.html', {'pedido': pedido})