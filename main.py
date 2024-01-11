estoque = []


def adicionar_produto(nome, preco, quantidade):
    produto = (nome, preco, quantidade)
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado ao estoque.")


def listar_estoque():
    print("\nEstoque Atual:")
    for produto in estoque:
        nome, preco, quantidade = produto
        print(f"\nNome do produto: {nome} \nPreço unitário: R${preco:.2f} \nQuantidade no estoque: {quantidade}")


def atualizar_estoque(nome, quantidade):
    for i, produto in enumerate(estoque):
        produto_nome, preco, estoque_atual = produto
        if produto_nome == nome:
            estoque[i] = (produto_nome, preco, estoque_atual + quantidade)
            print(f"Estoque de '{nome}' atualizado para {estoque_atual + quantidade}.")
            return
    print(f"Produto '{nome}' não encontrado.")


def calcular_valor_total():
    total = sum(preco * quantidade for _, preco, quantidade in estoque)
    print(f"\nValor total do estoque: R${total:.2f}")


while True:
    print("\nMenu de opções")
    print('1. Para inserir')
    print('2. Para listar')
    print('3. Para atualizar')
    print('4. Para ver o valor total')
    print('5. Para sair')

    escolha = input('Escolha uma opção acima: ')

    if escolha == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço unitário: "))
        quantidade = int(input("Quantidade em estoque: "))
        adicionar_produto(nome, preco, quantidade)

    elif escolha == '2':
        listar_estoque()

    elif escolha == '3':
        nome = input("Nome do produto para atualizar estoque: ")
        quantidade = int(input("Quantidade a ser adicionada ou retirada (use negativo para retirada): "))
        atualizar_estoque(nome, quantidade)

    elif escolha == '4':
        calcular_valor_total()

    elif escolha == '5':
        print("Até a próxima")
        break

    else:
        print("\nOpção inválida. Escolha uma das opções")
