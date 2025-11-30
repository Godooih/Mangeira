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
