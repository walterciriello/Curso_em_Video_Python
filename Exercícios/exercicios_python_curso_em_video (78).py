# método utilizando modulo "factorial"
'''from math import factorial
num = int(input('Digite um número: '))  
print(f'O fatorial de {num} é {factorial(num)}')'''


# solução utilizando método tradicional sem módulos
num = int(input('Digite um número: '))
c = num
f = 1 # fatorial recebe valor 1 (nulo) na multiplicação
print(f'Calculando {num}!')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
