from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador sortear um número
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*18)
jogador = (int(input('Em que número eu pensei? '))) # Jogador faz a escolha do número
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU! Eu pensei no número {}'.format(computador))
