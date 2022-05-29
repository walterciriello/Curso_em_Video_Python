from random import randint
comp = randint(0, 10)
print('''Óla, sou seu computador...
Vou pensar em um número entre 0 e 10! ''')
print('-=-' * 18)
print('Tente advinhar')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == comp:
       acertou = True
    elif jogador < comp:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
print(f'Você acertou com {palpites} tentativas')
