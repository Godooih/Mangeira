# 🪑 Mangeira & Mangeira | E-commerce Vintage

> Projeto de Backend para plataforma de venda de mobiliários vintage altamente sofisticados e de luxo.

O sistema gerencia o ciclo de vida dos produtos, desde o cadastro detalhado (com peças e medidas) até o processamento de pedidos, oferecendo uma API para consumo do frontend.

## 🚀 Funcionalidades

O projeto atende aos seguintes requisitos funcionais:

* **Gestão de Catálogo:**
    * Cadastro de produtos com integração automática na API.
    * Sistema de categorias (Jantar, Escritório, Sala, etc.).
    * Detalhamento técnico: Cadastro de múltiplas peças/componentes por produto (Medidas e Peso).
    * Cálculo automático de parcelamento e média de avaliações.
* **Gestão de Usuários:**
    * Extensão do usuário padrão do Django para incluir **CPF** e **Endereço Completo**.
* **Sistema de Pedidos:**
    * Carrinho de compras protegido (Requer login).
    * Fluxo de status do pedido (Em processamento, Aprovado, Enviado, Entregue, Devolução, etc.).
    * Registro de métodos de pagamento (PIX, Boleto, Cartão de Crédito).
    * *Nota Acadêmica:* Armazenamento didático de dados de cartão de crédito conforme requisito do projeto.
* **Segurança:**
    * Proteção de rotas sensíveis (Carrinho/Checkout).
    * Admin personalizado para gestão eficiente.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework:** Django
* **Banco de Dados:** SQLite (Padrão do Django)
* **Arquitetura:** MVT (Model-View-Template) adaptado para API.

## 📦 Como rodar o projeto

Siga os passos abaixo para executar o servidor de desenvolvimento na sua máquina:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU-USUARIO/mangeira-ecommerce.git](https://github.com/SEU-USUARIO/mangeira-ecommerce.git)
cd mangeira-ecommerce
2. Crie e ative o ambiente virtual (Recomendado)
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
Bash
pip install django
4. Configure o Banco de Dados
Bash
python manage.py makemigrations
python manage.py migrate
5. Crie um Superusuário (Admin)
Para acessar o painel administrativo:
Bash
python manage.py createsuperuser
# Siga as instruções para definir usuário e senha
6. Inicie o Servidor
Bash
python manage.py runserver
O projeto estará rodando em: http://127.0.0.1:8000/
________________________________________
🔌 Documentação da API
O backend fornece endpoints JSON para alimentar o frontend:
🛍️ Vitrine (Público)
Retorna todos os produtos ativos, com cálculo de parcelas e lista de peças inclusas.
•	URL: /api/vitrine/
•	Método: GET
•	Exemplo de Resposta:
JSON
{
  "produtos": [
    {
      "id": 1,
      "nome": "Poltrona Mole 1960",
      "categoria": "Sala de Estar",
      "preco": 15000.00,
      "parcelamento": "10x de R$ 1500.00 s/juros",
      "itens_inclusos": [
         {"nome": "Estrutura", "medidas": "100x80", "peso": "15kg"}
      ]
    }
  ]
}
🛒 Carrinho (Privado)
Acesso exclusivo para usuários logados. Retorna erro ou redireciona para login se não autenticado.
•	URL: /api/carrinho/
•	Método: GET
•	Autenticação: Requerida (Session/Login)
________________________________________
🗂️ Estrutura do Projeto
•	mangeira/: Configurações globais do projeto (settings, urls principais).
•	loja/: Aplicativo principal contendo a lógica de negócio.
o	models.py: Definição das tabelas (Produto, Cliente, Pedido).
o	views.py: Lógica das APIs e segurança.
o	admin.py: Customização do painel administrativo.
•	db.sqlite3: Banco de dados local.
✒️ Autor
•	Desenvolvedor: [Seu Nome Aqui]
•	Contexto: Projeto Acadêmico - Aplicações Web
________________________________________

### Dica Extra para o GitHub:
Se você quiser deixar o repositório ainda mais profissional, tire um "print" da tela do Admin (aquela onde aparecem os produtos e as peças que configuramos) e coloque na pasta do projeto. Depois, adicione essa imagem no README. Isso atrai muito a atenção de quem visita o perfil!

