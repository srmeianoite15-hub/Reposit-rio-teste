#15. Leia salário e percentual de reajuste. Calcule e exiba o valor de reajuste e o novo salario.

salario = float(input("Digite o valor de seu salário: "))
percentual = float(input("Digite o percentual de reajuste: "))
reajuste = salario * (percentual / 100)
salario_com_reajuste = salario + reajuste

print(f"Valor do reajuste: R$ {reajuste:.2f} ")
print(f"Novo salário: R$ {salario_com_reajuste:.2f}")
