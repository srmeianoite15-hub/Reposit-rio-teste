# contador = 1

# while contador <= 0:
#     idade = int(input("Informe a sua idade: "))
    
#     if idade <= 120:
#         print(f"você possui {idade} anos ").strip()
#         break
        
#     elif idade <= 0:
#         print("ERRO! Idade inserida não é válida")
        
#     else:
#         print("ERRO! A idade inserida não pode ser maior que 120 anos!")
        
#Usando o comando (or)

idade = int(input("Informe a sua idade: "))

while idade < 0 or idade > 120:
    
    print("ERRO! A idade inserida não é válida!")
    idade_ = int(input("Por favor informe uma idade válida: "))
      
print(f"Idade cadastrada com sucesso: {idade} anos ")

    
    
        