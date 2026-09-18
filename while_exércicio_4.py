
  
opcoes_do_menu = ["1 - cadastrar livo", "2 - Listar livros", "3 - Sair"]
lista_de_livros = []
            
while True:
    print("\n>>>> MENU <<<<")
    for contador in opcoes_do_menu:
        print(contador)
        
    opcao_escolhida = input("Selecione uma das opções: ")
    
    if opcao_escolhida =="1":
        quant_de_livros = int(input("Digite a quantidade de livros que deseja cadastrar: "))
            
        for l in range(1, quant_de_livros + 1):
            print(f">>>>> Livro: {l} >>>>> ")
            codigo_do_livro = input("Informe o código do seu livro: ").strip()
            titulo_do_livro = input("Informe o titulo do seu livro: ").strip()
            nome_do_autor = input("Informe o nome do autor do livro: ").strip()
            ano_de_lancamento_do_livro = int(input("Informe o ano de lançamento do livro: "))
            copia_do_livro = int(input("Informe quantas cópias serão castradas: "))
            
            if codigo_do_livro != "" or titulo_do_livro != "" or nome_do_autor != "" or ano_de_lancamento_do_livro > 0 or qtd_do_mesmo_livro > 0:
                dados_do_livro = [codigo_do_livro],[titulo_do_livro],[nome_do_autor],[ano_de_lancamento_do_livro],[copia_do_livro]
                lista_de_livros.append(dados_do_livro)
                print("Livro cadastrado com sucesso!")
            else:
                print("ERROR!! Verifique se você preencheu corretamente os campos! ")
                
    elif opcao_escolhida == "2":
        print("\n >>>> LISTA DE LIVROS CADASTRADOS <<<<")
        if not lista_de_livros:
            print("Nenhum livro cadastrado até o momento.")
        else:
            for livro in lista_de_livros:
                print(f"\ncodigo: {livro}", "\nTítulo: {livro}") 
        
    elif opcao_escolhida == "3":
        print("Saindo do Sistema... Até logo :)")
        break
    else:
        print("Opção inválida! Tente novamente.")
        