ordinais = ["primeiro","segunda","terceira","quarta"]
soma = 0.0

for i in range(1,5):
    nota = float(input("Digite a {ordinais} nota:  " ))
    soma = soma + nota
    
media = soma / 4
print(f"A media final é: {media:.2f}")
