from django.db import models
from django.contrib.auth.models import User

# 1. Criamos a tabela de Categorias PRIMEIRO (o Python lê de cima para baixo)
class Categoria(models.Model):
    nome = models.CharField(max_length=50) # Ex: "Escritório", "Sala"

    def __str__(self):
        return self.nome

# 2. Atualizamos o Produto para ter um "Link" com a Categoria
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    
    # Aqui está a mágica! Criamos o vínculo.
    # on_delete=models.SET_NULL: Se apagar a categoria "Sala", o produto não é apagado, só fica sem categoria.
    # null=True: Permite que o campo fique vazio (importante para não dar erro nos produtos que já existem).
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    # ... (mantenha seus métodos de get_parcelas e get_media_estrelas aqui) ...
    def get_parcelas(self):
        valor_parcela = self.preco / 10
        return f"10x de R$ {valor_parcela:.2f} s/juros"

    def get_media_estrelas(self):
        todas_avaliacoes = self.avaliacoes.all()
        if len(todas_avaliacoes) == 0:
            return 0
        soma_estrelas = 0
        for avaliacao in todas_avaliacoes:
            soma_estrelas += avaliacao.estrelas
        return soma_estrelas / len(todas_avaliacoes)

# ... (mantenha a classe Avaliacao igual) ...
class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, related_name='avaliacoes', on_delete=models.CASCADE)
    estrelas = models.IntegerField()
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"Nota {self.estrelas} para {self.produto.nome}"
    
class Peca(models.Model):
    # O elo de ligação: A peça pertence a um Produto
    produto = models.ForeignKey(Produto, related_name='pecas', on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=100) # Ex: "Tampo de Vidro"
    medidas = models.CharField(max_length=50) # Ex: "120cm x 80cm"
    peso = models.CharField(max_length=20) # Ex: "15kg"

    def __str__(self):
        return f"{self.nome} ({self.produto.nome})"
    
class Cliente(models.Model):
    # O OneToOneField diz: "Cada Usuário tem apenas UM Cliente associado"
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    
    cpf = models.CharField(max_length=14) # Ex: 123.456.789-00
    endereco = models.TextField() # Endereço completo cabe melhor num TextField
    
    # Obs: Nome e Email já existem dentro de 'usuario', não precisamos duplicar.
    
    def __str__(self):
        return f"Dados de {self.usuario.username}"
    
class Pedido(models.Model):
    # --- LISTAS DE OPÇÕES (CHOICES) ---
    # Isso cria aquele menu "drop-down" bonito no Admin
    
    METODOS_PAGAMENTO = [
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
        ('CARTAO', 'Cartão de Crédito'),
    ]

    STATUS_PEDIDO = [
        ('PROCESSAMENTO', 'Em Processamento'),
        ('APROVADO', 'Pagamento Aprovado'),
        ('NOTA_EMITIDA', 'Nota Fiscal Emitida'),
        ('PREPARACAO', 'Em Preparação'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGUE', 'Recebido/Entregue'),
        ('REPROVADO', 'Pagamento Reprovado'),
        ('CANCELADO', 'Cancelado'),
        ('SOLICITACAO_DEVOLUCAO', 'Solicitação de Devolução'),
        ('EM_DEVOLUCAO', 'Em Devolução'),
        ('DEVOLVIDO', 'Devolvido'),
        ('DEVOLUCAO_CANCELADA', 'Devolução Cancelada'),
    ]

    # --- CAMPOS DO PEDIDO ---
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    
    # Valores financeiros
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Configurações do Pedido
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)
    status = models.CharField(max_length=30, choices=STATUS_PEDIDO, default='PROCESSAMENTO')
    codigo_rastreio = models.CharField(max_length=50, blank=True, null=True)
    
    data_pedido = models.DateTimeField(auto_now_add=True) # Data automática de hoje

    # --- DADOS DO CARTÃO (REGRA 8) ---
    # Usamos blank=True e null=True porque se for PIX, esses campos ficam vazios.
    cartao_numero = models.CharField(max_length=16, blank=True, null=True)
    cartao_nome = models.CharField(max_length=100, blank=True, null=True)
    cartao_validade = models.CharField(max_length=5, blank=True, null=True) # Ex: 10/28
    cartao_codigo = models.CharField(max_length=3, blank=True, null=True)   # CVV

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"


class ItemPedido(models.Model):
    # Liga o item ao pedido "pai"
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    
    # Liga o item ao produto original
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    
    quantidade = models.IntegerField(default=1)
    
    # IMPORTANTE: Salvamos o preço aqui de novo.
    # Por quê? Se o produto custa 100 hoje e amanhã aumenta para 200,
    # o pedido antigo tem que continuar valendo 100. Isso é o "Preço Congelado".
    preco_na_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"