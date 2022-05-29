from datetime import date
nasc = int(input('Qual o ano de nascimento do atleta? '))
ano = date.today().year
idade = ano - nasc
print(f'O atleta tem \033[34m{idade}\033[m anos.')
if idade <= 9:
    print('Categotia: \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[34mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[34mJUNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[34mSÊNIOR\033[m')
else:
    print('Categoria: \033[34mMASTER\033[m')
