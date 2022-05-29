print('-'*30)
print('====== LOJAS GUANABARA =====')
print('-'*30)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
forma = int(input('Qual é a opção? '))
if forma == 1:
    print(f'Preço do produto é de \033[34m{preco-(preco*10/100):.2f}\033[m')
elif forma == 2:
    print(f'Preço do produto é de \033[34m{preco-(preco*5/100):.2F}\033[m')
elif forma == 3:
    print(f'Preço do produto é pe \033[34m{preco:.2f}\033[m')
elif forma == 4:
    print(f'Preço do produto é de \033[34m{preco+(preco*20/100):.2f}\033[m')
else:
    print('FORMA DE PAGAMENTO INVÁLIDA.')
