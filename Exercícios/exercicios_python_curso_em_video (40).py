nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}'.format((nome.upper())))
print('Seu nome em minúsculas: {}'.format((nome.lower())))
print('Seu nome possui: {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui: {} letras'.format(nome.find(' ')))




