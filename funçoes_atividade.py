bliblioteca = []


def calcular_total (preco, quantidade):
     total = preco * quantidade
     return total
    
def cadastrar_livro():
    print("\n >>> CADASTRO DE LIVROS <<<")
    
    quantidade_livros = int(input("Digite a quantidade de livros que deseja: "))
        
    for i in range(1, quantidade_livros + 1):
        print(f"\n >>> LIVRO {i} <<<")
        titulo = input("Informe o título do livro: ")
        autor = input("Informe a nome do autor: ")
        preco = float(input("Digite o preço do livro: "))
        quantidade = int (input("digite a quantidade de livros que deseja: "))
        
        valor = calcular_total(preco, quantidade)
        print(f"O valor total é {valor:.2f}")
        livro = [titulo, autor, preco, quantidade, valor]
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
         print(f" \n Quantidade total em estoque: {livro[4]:.2f}:")
        
def buscar_livro():
     print("\n >>> BUSCA DE LIVRO <<<")
     pesquisa = input("Informe o título do livro que você busca: ")
     encontrado = False
    
     for livro in bliblioteca:
         if pesquisa in livro[0].lower():
             print("[ENCONTRADO]")
             print(f"\n Título: {livro[0]}")
             print(f"\n Autor: {livro[1]}")
             print(f"\n Estoque: {livro[2]}")
             encontrado = True
            
     if not encontrado:
          print(f"Nenhum livro encotrado na bliblioteca!{pesquisa}...")
          
from datetime import datetime, date
          
def pedir_data(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            return date.today()
        try:
            return datetime. striptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.")
          
def devolver_livro():
    print("\n>>> AGENDAR DEVOLUÇÃO LIVRO <<<")
    titulo = input("Título do livro: ").lower()
    
    existe = any(livro[0].lower() == titulo for livro in bliblioteca)
    if not existe:
        print("Livro não encontrado!")
        return
    
    data = pedir_data("Data de Devolução (DD/MM/AAAA): ")
    if data < data.today():
        print("Escolha hoje ou uma data futura!")
        return
    
    devolver_livro.append({"título": titulo, "data": data})
    print(f"EScolha agendada para {data.strftime('%d/%m/%Y')}.")
    
def processar_devolução():
    hoje = date.today()
    pendente = []
    
    for d in devolver_livro:
        if d["data"] <= hoje:
            for livro in bliblioteca:
                if livro[0].lower() == d["titulo"]:
                    livro[3] += 1
                    print(f"[AUTO] '{livro[0]}' devolvido ao estoque!")
                    break
        else:
            pendente.append(d)
            
    devolver_livro[:] = pendente
        
                
    
        
    
def remover_livro():
     print("\n >>> REMOVER LIVRO <<<")
     pesquisa_de_remocao = input("Informe o título do livro que você deseja remover: ")
     encontrado = False
    
     for livro in bliblioteca:
         if pesquisa_de_remocao in livro[0].remove():
             print(f"\n Livro removido com sucesso {livro[0]}")
            
     if not encontrado:
             print("\nNenhum livro foi encontrado na bliblioteca!...\n")
        
    
            
        
def menu():
     while True:
         print("=>=>=> MENU PRINCIPAL <=<=<=")
         print("\n1- Cadasatrar Livros")
         print("2 - Listar Livros")
         print("3 - buscar livro")
         print("4 - Devolver livro")
         print("5 - Remover livro")
         print("6 - sair")
        
        
         opcao = input("Escolha uma opção: ")
        
         if opcao == "1":
             cadastrar_livro()
         elif opcao == "2":
             listar_ilvro()
         elif opcao == "3":
             buscar_livro()
         elif opcao == "4":
             devolver_livro()
         elif opcao == "5":
             remover_livro()
         elif opcao == "6":
             print("\n Saindo do programa.... :)")
             break
         else:
             print("\n Opção escolhida inválida! Tente novamente")
menu()       

        
