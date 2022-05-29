valor = float(input('Qual o valor do imóvel que deseja financiar? R$'))
sal = float(input('Qual o seu salário? R$'))
prazo = int(input('Em quantos anos deseja financiar o imóvel? '))
prest = valor/(prazo*12)
if prest >= sal*30/100:
    print('Você não pode realizar este financiamento!')
else:
    print(f'Parabéns, você pode realizar o financiamento! \nSua prestação será no valor de \033[34mR${prest:.2f}')
