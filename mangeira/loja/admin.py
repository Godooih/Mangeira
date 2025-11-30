from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Produto, Avaliacao, Categoria, Peca, Cliente, Pedido, ItemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# 2. ESSA CLASSE PRECISA EXISTIR (Configuração da tabela de peças)
class PecaInline(admin.TabularInline):
    model = Peca
    extra = 1 

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 0

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # 3. O PULO DO GATO ESTÁ AQUI EMBAIXO:
    # Você precisa colocar as duas classes dentro desta lista
    inlines = [PecaInline, AvaliacaoInline] 
    
    list_display = ('nome', 'categoria', 'preco', 'ativo')
    list_filter = ('ativo', 'categoria')


class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'Dados Pessoais (CPF/Endereço)'

# 2. Criamos um novo Admin de Usuário que mistura o original + o nosso
class UserAdmin(BaseUserAdmin):
    inlines = [ClienteInline]

# 3. Desregistramos o usuário original e registramos o nosso turbinado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0 # Não cria linhas vazias extras, só mostra o que tem
    # readonly_fields = ('preco_na_hora',) # Opcional: Para ninguém mudar o preço histórico

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ('id', 'usuario', 'status', 'valor_total', 'metodo_pagamento', 'data_pedido')
    list_filter = ('status', 'metodo_pagamento', 'data_pedido')
    
    # Organizamos os campos do cartão numa seção separada visualmente (Fieldsets)
    fieldsets = (
        ('Dados Gerais', {
            'fields': ('usuario', 'valor_total', 'valor_desconto', 'status', 'codigo_rastreio')
        }),
        ('Pagamento', {
            'fields': ('metodo_pagamento', 'cartao_numero', 'cartao_nome', 'cartao_validade', 'cartao_codigo')
        }),
    )