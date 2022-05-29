lanche = 'hambúrguer', 'suco', 'pizza', 'pudin'
#tuplas são imutáveis

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) # coloca a tupla em ordem

a = '2', '3', '4'
b = '1', '5', '6', '4'
c = a + b
print(c)
print(sorted(c))
print(len(c))
print(c.count(4))
print(c.index(5))
