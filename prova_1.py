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

    for n in range(1, quant_de_livros + 1):
        print(f">>>>> Livro >>>>> {n}")
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
    quant_de_alunos = int(input("Quantidade de alunos que deseja cadastrar? "))
    
    for a in range(1,quant_de_alunos +1):
        print(f">>>>> Aluno: >>>>> {a}")
        nome_do_aluno = input("Digite o nome do aluno que irá ser cadastrado: ").strip
        matricula_do_aluno = int(input("Digite o número de mátricula do aluno: "))
        turma = int(input("Digite a Turma do aluno: "))
        
    if nome_do_aluno != "" and matricula_do_aluno > 0 and turma > 0:
        

    




