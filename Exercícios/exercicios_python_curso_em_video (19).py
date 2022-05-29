print('-'*40)
print('Exercício nº 010')
print('-'*40)
rs = float(input('Qual o valor em reais deseja converter? R$ '))
cot = float(input('Qual a cotação atual do dolar? R$ '))
us = rs / cot
print('Com R${:.2f}, considerando a cotação atual de R${:.2f}, é possível comprar US${:.2f}.'.format(rs, cot, us))
print('-'*40)
