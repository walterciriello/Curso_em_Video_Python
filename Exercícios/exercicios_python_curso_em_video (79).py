print('Gerador de PA')
print('-='*8)
prim = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
termo = prim
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM')
