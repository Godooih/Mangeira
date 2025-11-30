from django.urls import path
from . import views

# Aqui definimos os "caminhos" que o navegador pode seguir
urlpatterns = [
    # Quando aceder a site.com/api/vitrine/, chama a função vitrine_produtos
    path('api/vitrine/', views.vitrine_produtos, name='vitrine'),
    
    # Quando aceder a site.com/api/carrinho/, chama a função ver_carrinho
    path('api/carrinho/', views.ver_carrinho, name='carrinho'),
]