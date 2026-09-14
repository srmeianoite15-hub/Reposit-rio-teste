repeticoes = 100

for r in range(repeticoes):

    print("\n----------------------------")
    print("\n BEM-VINDO À BLIBLIOTECA ")
    print("\n----------------------------")

    print("\n O que deseja fazer hoje?\n ")

    print("1 - Cadastro de Livro. ")
    print("2 - Cadastro de Alunos.")
    print("3 - Realização de Emprestimo.")
    print("4 - Sair.")

    escolha_da_opcao = input("\n Escolha uma das opções: ")

    if escolha_da_opcao == "1":
        quant_de_livros = int(input("\n Quantidade de livros que deseja cadastrar? "))

        for l in range(1, quant_de_livros + 1):
            print(f">>>>> Livro: {l} >>>>> ")
            codigo_do_livro = input("Informe o código do seu livro: ").strip
            titulo_do_livro = input("Informe o titulo do seu livro: ").strip
            nome_do_autor = input("Informe o nome do autor do livro: ").strip
            ano_de_lancamento_do_livro = int(input("Informe o ano de lançamento do livro: "))
            qtd_do_mesmo_livro = int(input("Informe quantas cópias serão castradas: "))
    
        if codigo_do_livro != "" and titulo_do_livro != "" and nome_do_autor != "" and ano_de_lancamento_do_livro > 0 and qtd_do_mesmo_livro > 0:
            print("Livro cadastrado com sucesso!")
        else:
            print("ERROR!! Verifique se você preencheu corretamente os campos! ")

    elif  escolha_da_opcao == "2":
        quant_de_alunos = int(input("\n Quantidade de alunos que deseja cadastrar? "))
    
        for a in range(1,quant_de_alunos +1):
            print(f"\n>>>>> Aluno: {a} >>>>> \n")
            nome_do_aluno = input("Digite o nome do aluno que irá ser cadastrado: ").strip
            matricula_do_aluno = (input("Digite o número de mátricula do aluno: "))
            turma = (input("Digite a Turma do aluno: "))
            
        if nome_do_aluno != "" and matricula_do_aluno != "" and turma !="":
            print("O Aluno foi cadastrado com sucesso! :) " )
        else:
            print("Aconteu um erro no cadstro do auno ): . Por favor revise se inseriu os dados corretos!")

    elif escolha_da_opcao == "3":
        print("\n>>>>> Emprestimo >>>>>\n ")
        codigo_do_livro = input("Informe o código do livro: ").strip
        matricula_do_aluno = input("Informe o número da sua matrícula: ")

        if codigo_do_livro !="" and matricula_do_aluno !="":
            quant_disponivel_de_livros = int(input("Quantidade de livros que deseja emprestar: "))

            if quant_disponivel_de_livros > 0:
                print("Emprestimo realizado com sucesso! :)")
            else:
                print("Não foi possível realizar o emprestimo! ): \n Não há exemplares disponíveis.")

        else:
            print("Erro! código do livro e matrícula do aluno devem ser informados!")

    elif escolha_da_opcao == "4":
        print("Saindo do sistema... Nos vemos depois! ")
    
    else:
        print("Opção inválida! Por favor selecione uma das opções 1, 2, 3, ou 4.")
            


        

    




