sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados iválidos. Por favor, digite seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo \033[34m{sexo}\033[m registrado com sucesso.')
