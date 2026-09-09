#16. Leia o preço de um produto e calcule o valor com 10% de desconto.

preco = float(input("Digite o valor do produto:R$ "))

desconto = preco * 0.10
preco_com_desconto = preco - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor do produto com desconto: R$ {preco_com_desconto:.2f}")
