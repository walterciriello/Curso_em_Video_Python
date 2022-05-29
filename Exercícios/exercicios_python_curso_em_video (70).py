num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divissível {total} vezes.')
if total == 2:
    print(f'Ele é um NÚMERO PRIMO.')
else:
    print('Ele NÃO É UM NÚMERO PRIMO.')
