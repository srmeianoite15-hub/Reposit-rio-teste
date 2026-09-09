produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponível em estoque: "))

if quantidade == 0:
    situação_do_estoque = "Produto esgotado"
elif quantidade <= 7:
    situação_do_estoque = "Estoque crítico por falta de produtos"
elif quantidade <= 20:
    situação_do_estoque = "Estoque baixo para suprir a demanda"
else:
    situação_do_estoque = "Estoque normal"

print("\n-----SITUAÇÃO DO ESTOQUE-----\n")
print(f"Produto: {produto}")
print(f"Quantidade disponivel do produto: {quantidade}")
print(f"Situação: {situação_do_estoque}")