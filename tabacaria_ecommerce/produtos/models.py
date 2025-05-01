# produtos/models.py
from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    imagem = models.ImageField(upload_to='categorias/', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('produtos:lista_por_categoria', args=[self.slug])
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    estoque = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('produtos:detalhe_produto', args=[self.slug])
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']