print('--- Gerador de PA ----')
print('-='*10)
prim = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progresão finalizanda com {total} termos mostrados.')
print('FIM')
