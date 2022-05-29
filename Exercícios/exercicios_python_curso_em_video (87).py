print('-'*25)
print('CADASTRE UMA PESSOA')
print('-'*25)
maiores = mulheres = homens = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continaur? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-'*25)
print(f'{maiores} são maiores de 18 anos.')
print(f'{homens} são homens.')
print(f'{mulheres} mulheres tem menos de 20 anos.')
