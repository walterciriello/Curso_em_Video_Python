num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} convertifo para binário é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif base ==3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Escolha de base inválida! Tente novamente.')
