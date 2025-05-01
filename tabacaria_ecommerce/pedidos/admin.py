from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['produto']
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cidade', 'pago', 'status', 'data_criacao']
    list_filter = ['pago', 'status', 'data_criacao']
    search_fields = ['nome', 'email', 'id']
    inlines = [ItemPedidoInline]
    list_editable = ['status', 'pago']