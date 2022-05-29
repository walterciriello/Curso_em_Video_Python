print('-='*14)
print('NÚMEROS PARES ENTRE 1 E 50:')
print('-='*14)
for c in range(2, 51, 2):
        print('.', end=' ')
        print(c)

for c in range(1, 51): # neste caso o processor vai fazer o dobro de verificações
    print('.', end=' ')
    if c % 2 == 0:
         print (c)
