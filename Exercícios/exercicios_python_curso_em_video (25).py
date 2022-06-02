# Exercise number 25

salario = float(input("Digite o salário do funcionário: R$ "))
aumento = 0
aumento += salario * 15 / 100
novo_salario = salario + aumento
print(f"O salário do funcionário após os 15% de aumento será de R${novo_salario:.2f}")
