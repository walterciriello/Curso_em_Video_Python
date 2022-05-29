print('-'*40)
print('Exercício nº 014')
print('-'*40)
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
#devido a ordem de precedência não é necessáio os parenteses.
print('A temperatura de {:.2f}Cº corresponde a {:.2f}ºF'.format(c, f))
print('-'*40)
