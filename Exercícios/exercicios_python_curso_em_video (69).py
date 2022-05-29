print('-='*15)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('-='*15)
termo = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
decimo = termo + (11 -1) * razao
for c in range(termo, decimo, razao):
    print(f'{c}', end=' - ')
print('ACABOU!')
