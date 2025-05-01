# produtos/urls.py
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('categoria/<slug:categoria_slug>/', views.lista_produtos, name='lista_por_categoria'),
    path('<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
]