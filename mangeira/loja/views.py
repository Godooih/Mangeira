from django.http import JsonResponse
# Esse é o "porteiro" que bloqueia quem não está logado
from django.contrib.auth.decorators import login_required 
from .models import Produto

def vitrine_produtos(request):
    produtos = Produto.objects.filter(ativo=True)
    lista_dados = []

    for item in produtos:
        # --- Lógica nova das Peças ---
        pecas_do_produto = []
        for peca in item.pecas.all():
            pecas_do_produto.append({
                "nome": peca.nome,
                "medidas": peca.medidas,
                "peso": peca.peso
            })
        # -----------------------------

        dados = {
            "id": item.id,
            "nome": item.nome,
            "categoria": item.categoria.nome if item.categoria else "Sem Categoria",
            "estrelas": item.get_media_estrelas(),
            "quantidade_avaliacoes": item.avaliacoes.count(),
            "preco": float(item.preco),
            "parcelamento": item.get_parcelas(),
            
            # Adicionamos a lista de peças aqui no final
            "itens_inclusos": pecas_do_produto,
            
            "botao_adicionar": True
        }
        lista_dados.append(dados)

    return JsonResponse({"produtos": lista_dados})

# --- ROTA PRIVADA (Só logado vê) ---
# Se tentar acessar sem logar, vai ser redirecionado para o login do admin
@login_required(login_url='/admin/login/') 
def ver_carrinho(request):
    usuario = request.user
    
    return JsonResponse({
        "status": "sucesso",
        "usuario": usuario.username,
        "mensagem": "Você está logado e pode ver o carrinho."
    })