livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Quantidades de livro")
    print("6 - Sair")
#Foi adicionado a opção de "Quantidades de livros".

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")
        encontrado = False
        #Foi feita a adição de variável "encontrado" para fazer o rastreamento do livro, e saber se o livro foi encontrado.

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                encontrado = True
                break

        if not encontrado:
            print("Não foi encontrado nenhum livro correspondente!")
        #Comando if not para informar caso a pesquisa falhe    

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        encontrado = False
        #para rastrear se exclusão ocorreu

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                print("Livro excluído!")
                encontrado = True
                break
            #utilização da função break para finalizar o laço e evitar modificações na lista

    elif opcao == "5":
        print(f"\n Mostrar a quantidade de livros castrados: {len(livros)}")
        #Uso da função len para fazer a contabilização dos registros na lista


    elif opcao == "6":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")