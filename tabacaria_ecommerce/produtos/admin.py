# produtos/admin.py
from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'estoque', 'disponivel', 'destaque']
    list_filter = ['disponivel', 'destaque', 'categoria']
    list_editable = ['preco', 'estoque', 'disponivel', 'destaque']
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ['nome', 'descricao']