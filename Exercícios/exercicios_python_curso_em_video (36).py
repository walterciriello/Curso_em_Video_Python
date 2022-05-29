from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
print(f'O SENO de {angulo} é \033[34m{sin(radians(angulo)):.2f}\033[m')
print(f'O COSSENO de {angulo} é \033[34m{cos(radians(angulo)):.2f}\033[m')
print(f'A TANGENTE de {angulo} é \033[34m{tan(radians(angulo)):.2f}\033[m')
