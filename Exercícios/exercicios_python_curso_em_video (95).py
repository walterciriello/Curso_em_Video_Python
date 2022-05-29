# não consegui executar da foma que gostaria
#cadastrar produtos e ao final gerar a lista

while True:
    lista = (str(input('Digite o produto: '))), \
            (str(input('Valor do produto: R$ ')))
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Cadastar mais um produto? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
while True:
    for pos in range(0, len(lista)):
        if pos % 2 == 0:
            print(F'{lista[pos]:.<30}', end='')
        else:
            print(f'R$ {lista[pos]:.>}')
