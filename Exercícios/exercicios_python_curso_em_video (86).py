from random import randint
print('~'*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('~'*25)
cont = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(1, 10)
    soma = jog + comp
    poui = ' '
    while poui not in 'PI':
        poui = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-' * 25)
    print(f'Vôce jogou {jog} e o computador {comp}. Toatal foi {soma} ', end='')
    print(f'DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if poui == 'P':
        if soma % 2 == 0:
           print('Vôce VENCEU!')
           cont += 1
        else:
            print('Vôce PERDEU!')
            break
    elif poui == 'I':
        if soma % 2 == 1:
            print('Vôce VENCEU!')
            cont += 1
        else:
            print('Voê PERDEU!')
            break
    print('-'*25)
    print('Vamos jogar novamente...')
    print('~'*25)
print(f'GAME OVER!!! Você venceu {cont} vezes.')
