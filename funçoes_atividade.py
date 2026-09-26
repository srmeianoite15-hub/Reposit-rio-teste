bliblioteca = []


# def calcular_total (preco, quantidade):
#      total = preco * quantidade
#      return total

livro = input("Digite o nome do livro: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

for l in livro(1,livro + 1):
    print(input("Digite a quantidade de livros que deseja: "))
    
    def calcular_total (preco, quantidade):
     total = preco * quantidade
     return total

livro = input("Digite o nome do livro: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))


valor = calcular_total(preco, quantidade)
print(f"O valor total é {valor:.2f}")

# def cadastrar_livro():
#      print("\n >>> CADASTRO DE LIVROS <<<")
#      titulo = input("Informe o título do livro: ")
#      autor = input("Informe a nome do autor: ")
#      preco = float(input("Digite o preço do livro: "))
#      quantidade = int (input("digite a quantidade de livros que deseja: "))
    
#      valor_estoque =  calcular_total(preco, quantidade)
    
#      livro = [titulo, autor, preco, quantidade, valor_estoque]
    
#      bliblioteca.append(livro)
#      print(f"livro '{titulo}' cadastrado com sucesso!")
    
# def listar_ilvro():
#      print("\n >>> LISTA DE LIVROS <<<")
#      if not bliblioteca:
#          print("Nenhum livro cadastrado até o momento")
#          return
#      for contador, livro in enumerate(bliblioteca, 1):
#          print(f" \n livro: {contador}")
#          print(f" \n Título: {livro[0]}")
#          print(f" \n Autor: {livro[1]}")
#          print(f" \n Preço: {livro[2]}:2.f")
#          print(f" \n Quantidade: {livro[3]}")
#          print(f" \n Quantidade total em estoque: {livro[4]}:2.f")
        
# def buscar_livro():
#      print("\n >>> BUSCA DE LIVRO <<<")
#      pesquisa = input("Informe o título do livro que você busca: ")
#      encontrado = False
    
#      for livro in bliblioteca:
#          if pesquisa in livro[0].lower():
#              print("[ENCONTRADO]")
#              print(f"\n Título: {livro[0]}")
#              print(f"\n Autor: {livro[2]}")
#              print(f"\n Estoque: {livro[3]}")
#              encontrado = True
            
#      if not encontrado:
#           print(f"Nenhum livro encotrado na bliblioteca!{pesquisa}...")
         
# def remover_livro():
#      print("\n >>> REMOVER LIVRO <<<")
#      pesquisa_de_remocao = input("Informe o título do livro que você deseja remover: ")
#      encontrado = False
    
#      for livro in bliblioteca:
#          if pesquisa_de_remocao in livro[0].remove():
#              print(f"\n Livro removido com sucesso {livro[0]}")
            
#      if not encontrado:
#              print("\nNenhum livro foi encontrado na bliblioteca!...\n")
        
    
            
        
# def menu():
#      while True:
#          print("=>=>=> MENU PRINCIPAL <=<=<=")
#          print("\n1- Cadasatrar Livros")
#          print("2 - Listar Livros")
#          print("3 - buscar livro")
#          print("4 - Remover livro")
#          print("5 - Sair")
        
        
#          opcao = input("Escolha uma opção: ")
        
#          if opcao == "1":
#              cadastrar_livro()
#          elif opcao == "2":
#              listar_ilvro()
#          elif opcao == "3":
#              buscar_livro()
#          elif opcao == "4":
#              remover_livro()
#          elif opcao == "5":
#              print("\n Saindo do programa.... :)")
#              break
#          else:
#              print("\n Opção escolhida inválida! Tente novamente")
# menu()       

        
