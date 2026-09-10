nome_do_aluno = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
resposta_do_cadastro = input("Possui cadastro ativo (sim/não): ").strip().lower()
 
cadastro_ativo = resposta_do_cadastro == 'sim'
 
if not cadastro_ativo:
     situacao = "Acesso negado"
elif idade <= 14:
    situacao = "Acesso permitido"
else:
    situacao = "Acesso permitido"
    
print("\n----- VALIDAÇÃO DE ACESSO ----\n")
print(f"Aluno: {nome_do_aluno}")
print(f"Situação: {situacao}")
