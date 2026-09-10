cliente = input("Digite seu nome: ")
velocidade_contratada = float(input("Digite a velocidade contratada em Mbs: "))

if velocidade_contratada <= 50:
    plano = ("Plano básico")
elif velocidade_contratada <= 199:
    plano = ("Plano intermediário")
elif velocidade_contratada <=499:
    plano = ("Plano avançado")
else:
    plano = ("Plano ultra")

print("\n-----Clássificação de Plano-----\n")
print(f"Cliente: {cliente}")
print(f"Velocidade da internet: {velocidade_contratada} mbs")
print(f"Plano adquirido: {plano}")