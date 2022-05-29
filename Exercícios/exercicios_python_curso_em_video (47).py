vel = int(input('Qual a velocidade do veículo: '))
if vel > 80:
    multa = 7 * (vel - 80)
    print('Você está acima do limite de  velocidade! \nReceberá uma multa no valor de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
