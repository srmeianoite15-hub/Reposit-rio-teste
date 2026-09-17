alunos = ["João", "Pedro", "Maria"]

for contador in alunos:
    print(contador)
    
adicionar_alunos = int(input("Quantos alunos deseja adicionar: "))

for n in range(1, adicionar_alunos + 1) :
    print(f"\n>>> LISTA DE ALUNOS {alunos}>>>")
    print(input(f"\n Digite o nome do aluno: "))
    alunos.append(adicionar_alunos)
    
print("\n >>> LISTA DE ALUNOS ATUALIZADA <<<")
for aluno in alunos:
    print(aluno)
    
#segunda forma
    
alunos = ["João", "Pedro", "Maria"]

for contador in alunos:
    print(contador)
    
adicionar_alunos = int(input("Quantos alunos deseja adicionar: "))

for n in range(1, adicionar_alunos + 1) :
    print(f">>>>> ALUNO {n} >>>>> ")
    adicionar_alunos = input("Digite o nome do aluno: ").strip()
    alunos.append(adicionar_alunos)
    
print("\n >>>> LISTA DE ALUNOS ATUALIZADA >>> ")
for aluno in alunos:
    print(aluno)