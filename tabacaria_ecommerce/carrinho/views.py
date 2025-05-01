from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .cart import Carrinho
from .forms import CarrinhoAddProdutoForm

@require_POST
def carrinho_adicionar(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = CarrinhoAddProdutoForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.adicionar(produto=produto,
                          quantidade=cd['quantidade'],
                          substituir_quantidade=cd['substituir'])
    
    return redirect('carrinho:detalhe_carrinho')

def carrinho_remover(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)
    return redirect('carrinho:detalhe_carrinho')

def detalhe_carrinho(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['form_atualizar'] = CarrinhoAddProdutoForm(initial={
            'quantidade': item['quantidade'],
            'substituir': True})
    
    return render(request, 'carrinho/detalhe.html', {'carrinho': carrinho})