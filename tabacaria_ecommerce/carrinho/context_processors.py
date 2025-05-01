from .cart import Carrinho

def carrinho(request):
    """
    Context processor que disponibiliza o carrinho em todos os templates
    """
    return {'carrinho': Carrinho(request)}