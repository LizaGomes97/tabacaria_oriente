from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos', null=True, blank=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f'Pedido {self.id}'
    
    def get_total(self):
        """
        Calcula o valor total do pedido
        """
        return sum(item.get_custo() for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)
    
    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
    
    def __str__(self):
        return f'{self.id}'
    
    def get_custo(self):
        """
        Calcula o custo do item
        """
        return self.preco * self.quantidade