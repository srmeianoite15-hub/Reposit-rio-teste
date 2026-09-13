nome = input("Digite seu nome: ")

tipo_de_problema =  ("Informe o tipo de problema que está ocorrendo: ")
print("1 - Não liga / Está fumaçando / Fazendo barulho alto")
print("2 - Liga, mas apresenta travamentos / Liga mas reinicia após ligar")
print("3 - programa não está entrando / programa sai sozinho ")
print("4 - Dúvidas sobre configuração / Avaria ná carcaça da máquina")
opcao = input("Digite a opção de 1 á 4 de acordo com seu problema: ")

if opcao == "1":
    problema = "equipamento inoperante"
    prioridade = "crítica"
elif opcao == "2":
    problema = "instabilidade no funcionamento da máquina"
    prioridade = "alta"
elif opcao == "3":
    problema = "falha no funcionamento de programas e má otimização"
    prioridade = "baixa"
elif opcao == "4":
    problema = "Dúvidas"
    prioridade = "baixa"
else:
    problema = None # Indique a uma opção valida

if problema is not None:
    tempo_de_problema = input("A quanto tempo o problema está ocorrendo? ")
    
    print(f"Usúario: {nome}")
    print(f"Incidente relatado {problema}, relatado há {tempo_de_problema}")
    print(f"Prioridade: {prioridade}")
else:
    print("opção inavalida! Por favor digite uma opção valida")
    
# Usando laço para que cada vez que o usúario digitar uma opção invalida ele seja redirecionado para a váriavel opcao.

tipo_de_problema =  ("Informe o tipo de problema que está ocorrendo: ")
print("1 - Não liga / Está fumaçando / Fazendo barulho alto")
print("2 - Liga, mas apresenta travamentos / Liga mas reinicia após ligar")
print("3 - programa não está entrando / programa sai sozinho ")
print("4 - Dúvidas sobre configuração / Avaria ná carcaça da máquina")

while True:
    opcao = input("Digite a opção de 1 á 4 de acordo com seu problema: ")

    if opcao == "1":
        problema = "equipamento inoperante"
        prioridade = "crítica"
        break # Sai do laço while
    elif opcao == "2":
        problema = "instabilidade no funcionamento da máquina"
        prioridade = "alta"
        break # Sai do laço while
    elif opcao == "3":
        problema = "falha no funcionamento de programas e má otimização"
        prioridade = "baixa"
        break # Sai do laço while
    elif opcao == "4":
        problema = "Dúvidas"
        prioridade = "baixa"
        break # Sai do laço while
    else:
        print("opção inválida! Digite uma opção válida")
    

tempo_de_problema = input("A quanto tempo o problema está ocorrendo? ")
    
print(f"Usúario: {nome}")
print(f"Incidente relatado {problema}, relatado há {tempo_de_problema}")
print(f"Prioridade: {prioridade}")
