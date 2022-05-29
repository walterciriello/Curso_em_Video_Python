from math import radians, sin, cos, tan
print('-'*40)
print('Exercício nº 018')
print('-'*40)
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(a, tan(radians(a))))
print(''*40)
