nome = input("Digite seu nome: ")

tipo_de_problema =  ("Informe o tipo de problema que está ocorrendo: ")
print("1 - Não liga / Está fumaçando / Fazendo barulho alto")
print("2 - Liga, mas apresenta travamentos / Liga mas reinicia após ligar")
print("3 - programa não está entrando / programa sai sozinho ")
print("4 - Dúvidas sobre configuração / Avaria ná carcaça da máquina")
opcao = input("Digite a opção de 1 á 4 de acordo com seu problema: ")

tempo_de_problema = input("A quanto tempo o problema está ocorrendo? ")

if opcao == "1":
    problema = "equipamento inoperante"
    prioridade = "crítica"
elif opcao == "2":
    problema = "instabilidade no funcionamento da máquina"
    prioridade = "alta"
elif opcao == "3":
    problema = "falha no funcionamento de programas e má otimização"
    prioridade = "baixa"
else:
    problema = "Dúvidas"
    prioridade = "baixa"
    
print(f"Usúario: {nome}")
print(f"Incidente relatado {problema}, relatado há {tempo_de_problema}")
print(f"Prioridade: {prioridade}")