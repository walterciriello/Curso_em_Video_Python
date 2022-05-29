'''print('-'*40)
print('Exercício nº 017')
print('-'*40)
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_ad = float(input('Digite o valor do cateto adjacente: '))
hi = (cat_op ** 2 + cat_ad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
print('-'*40)'''

# outra alternativa:

import math
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_ad = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(cat_op, cat_ad)
print('A medida da hipotenusa é {:.2f}'.format(hi))
