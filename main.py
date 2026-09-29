# =========================================================
# TRABALHO PRÁTICO - ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos de Lanchonete
# =========================================================

def exibir_cardapio():
    """Exibe os produtos disponíveis na lanchonete."""
    print("\n" + "=" * 40)
    print("           CARDÁPIO DA LANCHONETE          ")
    print("=" * 40)
    print("Código | Produto                | Preço")
    print("-" * 40)
    print("  1    | X-Burguer              | R$ 15.00")
    print("  2    | X-Salada               | R$ 18.00")
    print("  3    | Batata Frita           | R$ 12.00")
    print("  4    | Refrigerante           | R$  6.00")
    print("  5    | Suco Natural           | R$  8.00")
    print("=" * 40)

def obter_preco_produto(codigo):
    """
    Retorna o preço do produto com base no código fornecido.
    Retorna -1.0 caso o código seja inválido.
    """
    match codigo:
        case "1":
            return 15.00
        case "2":
            return 18.00
        case "3":
            return 12.00
        case "4":
            return 6.00
        case "5":
            return 8.00
        case _:
            return -1.0

def calcular_desconto(total_bruto):
    """
    Aplica as regras de desconto com base no valor total bruto:
    - Menor que R$ 50.00: 0%
    - De R$ 50.00 até R$ 99.99: 5%
    - R$ 100.00 ou mais: 10%
    Retorna a porcentagem e o valor em reais do desconto.
    """
    if total_bruto < 50.00:
        percentual = 0
    elif total_bruto <= 99.99:
        percentual = 5
    else:
        percentual = 10
    
    valor_desconto = total_bruto * (percentual / 100)
    return percentual, valor_desconto

def selecionar_forma_pagamento():
    """Solicita e valida a forma de pagamento selecionada pelo cliente."""
    while True:
        print("\nEscolha a forma de pagamento:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Opção desejada (1-3): ").strip()

        if opcao == "1":
            return "Dinheiro"
        elif opcao == "2":
            return "PIX"
        elif opcao == "3":
            return "Cartão"
        else:
            print("[ERRO] Opção de pagamento inválida! Tente novamente.")

def exibir_resumo(nome, total_bruto, percentual, valor_desconto, valor_final, pagamento):
    """Exibe o recibo/resumo final do pedido."""
    print("\n" + "=" * 40)
    print("            RESUMO DO PEDIDO               ")
    print("=" * 40)
    print(f"Cliente:            {nome}")
    print(f"Valor Original:     R$ {total_bruto:.2f}")
    print(f"Desconto Aplicado:  {percentual}%")
    print(f"Valor do Desconto:  R$ {valor_desconto:.2f}")
    print(f"Valor Final:        R$ {valor_final:.2f}")
    print(f"Forma de Pagamento: {pagamento}")
    print("=" * 40)
    print("Obrigado pela preferência! Volte sempre.\n")

def executar_sistema():
    """Função principal que gerencia o fluxo do atendimento."""
    print("=== SISTEMA DE ATENDIMENTO E PEDIDOS ===")
    nome_cliente = input("Por favor, digite o seu nome: ").strip()
    
    # Garante que o nome não fique em branco
    while not nome_cliente:
        nome_cliente = input("Nome inválido. Digite seu nome: ").strip()

    total_compra = 0.0
    continuar = "s"

    # Laço principal de repetição dos pedidos
    while continuar.lower() == "s":
        exibir_cardapio()
        codigo = input("Digite o código do produto desejado: ").strip()
        preco = obter_preco_produto(codigo)

        if preco == -1.0:
            print("[ERRO] Código de produto inválido! Nenhum item foi adicionado.")
        else:
            try:
                qtd = int(input("Digite a quantidade desejada: "))
                if qtd > 0:
                    subtotal = preco * qtd
                    total_compra += subtotal
                    print(f"-> Item adicionado com sucesso! Subtotal: R$ {subtotal:.2f}")
                else:
                    print("[ERRO] A quantidade deve ser maior que zero!")
            except ValueError:
                print("[ERRO] Quantidade inválida! Digite apenas números inteiros.")

        continuar = input("\nDeseja adicionar outro produto? (S/N): ").strip()

    # Verifica se o cliente comprou algo antes de ir para o pagamento
    if total_compra > 0:
        percentual, valor_desconto = calcular_desconto(total_compra)
        valor_final = total_compra - valor_desconto
        forma_pagamento = selecionar_forma_pagamento()
        
        exibir_resumo(nome_cliente, total_compra, percentual, valor_desconto, valor_final, forma_pagamento)
    else:
        print(f"\nAtendimento cancelado para {nome_cliente}. Nenhum produto selecionado.")

# Ponto de entrada do programa
if __name__ == "__main__":
    executar_sistema()