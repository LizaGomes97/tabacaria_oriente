from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.register, name='registro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('perfil/', views.profile, name='perfil'),
]