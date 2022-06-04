#":.2f" utilizado para formatar o resultado em duas casas decimais

number = int(input('Digite um número:\n'))
dobro = number * 2
triplo = number * 3
raiz = number ** (1/2)

print(f"O dobro de {number} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}")
