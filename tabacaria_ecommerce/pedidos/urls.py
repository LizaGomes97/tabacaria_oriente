from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('meus-pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('meus-pedidos/<int:pedido_id>/', views.detalhe_pedido, name='detalhe_pedido'),
]