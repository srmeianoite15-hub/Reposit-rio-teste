bliblioteca = []


def calcular_total (preco, quantidade):
    total = preco * quantidade
    return total

def cadastrar_livro():
    print("\n >>> CADASTRO DE LIVROS <<<")
    titulo = input("Informe o título do livro: ")
    autor = input("Informe a nome do autor: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade = int (input("digite a quantidade de livros que deseja: "))
    
    valor_estoque =  calcular_total(preco, quantidade)
    
    livro = [titulo, autor, preco, quantidade, valor_estoque]
    
    bliblioteca.append(livro)
    print(f"livro '{titulo}' cadastrado com sucesso!")
    
def listar_ilvro():
    print("\n >>> LISTA DE LIVROS <<<")
    if not bliblioteca:
        print("Nenhum livro cadastrado até o momento")
        return
    for contador, livro in enumerate(bliblioteca, 1):
        print(f" \n livro: {contador}")
        print(f" \n Título: {livro[0]}")
        print(f" \n Autor: {livro[1]}")
        print(f" \n Preço: {livro[2]}:2.f")
        print(f" \n Quantidade: {livro[3]}")
        print(f" \n Quantidade total em estoque: {livro[4]}:2.f")
        
def menu():
    while True:
        print("=>=>=> MENU PRINCIPAL <=<=<=")
        print("\n1- Cadasatrar Livros")
        print("2 - Listar Livros")
        print("4 - Sair")
        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_ilvro()
        #elif opcao == "3":
            #buscar_livro
        elif opcao == "4":
            print("\n Saindo do programa.... :)")
            break
        else:
            print("\n Opção escolhida inválida! Tente novamente")
menu()       

        
