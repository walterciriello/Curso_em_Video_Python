from random import shuffle
print('-'*40)
print('Exercício nº 020')
print('-'*40)
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será {}'. format(lista))
print('-'*40)
