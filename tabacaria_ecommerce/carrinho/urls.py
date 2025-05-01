# carrinho/urls.py
from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.detalhe_carrinho, name='detalhe_carrinho'),
    path('adicionar/<int:produto_id>/', views.carrinho_adicionar, name='carrinho_adicionar'),
    path('remover/<int:produto_id>/', views.carrinho_remover, name='carrinho_remover'),
]