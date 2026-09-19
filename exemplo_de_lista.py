 #
# alunos = ["João", "Pedro", "Maria"]

# for contador in alunos:
#     print(contador)
    
# adicionar_alunos = int(input("Quantos alunos deseja adicionar: "))

# for n in range(1, adicionar_alunos + 1) :
#     print(f"\n>>> LISTA DE ALUNOS {alunos}>>>")
#     print(input(f"\n Digite o nome do aluno: "))
#     alunos.append(adicionar_alunos)
    
# print("\n >>> LISTA DE ALUNOS ATUALIZADA <<<")
# for aluno in alunos:
#     print(alunos)
    
#segunda forma
    
alunos = ["João", "Pedro", "Maria "]
print("\n >>>>> LISTA ATUAL DE ALUNOS >>>>>")

print()
for contador in alunos:
    print(contador)
    
while True:
    try:
    
        adicionar_alunos = int(input("\nQuantos alunos deseja adicionar: "))
    
        if adicionar_alunos > 0:
            break
        elif adicionar_alunos == 0:
            print("Erro! Nenhum aluno será castrado! ")
            break
        else:
            print("Erro! informe o n° de alunos que serão cadastrados: ")
    
    except ValueError:
        print("Erro! Você digitou letras ou textos. Por favor, digite apenas números inteiros!")    

for n in range(1, adicionar_alunos + 1) :
    print(f"\n>>>>> ALUNO {n} >>>>> \n")
    adicionar_alunos = input("Digite o nome do aluno: ").strip()
    alunos.append(adicionar_alunos)
    
    
print("\n >>>> LISTA DE ALUNOS ATUALIZADA >>> \n")
for aluno in alunos:
    print(aluno)
    print()