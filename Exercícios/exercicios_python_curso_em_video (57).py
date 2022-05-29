from datetime import date
nasc = int(input('Qual seu ano de nascimento? '))
ano = date.today().year
print(f'Você esta com \033[34m{ano-nasc}\033[m anos.')
if ano-nasc < 18:
    print(f'Deverá se alistar ao serviço militar \033[34m{ano+(18-(ano-nasc))}\033[m daqui \033[34m{18-(ano-nasc)}\033[m ano(s).')
elif ano-nasc == 18:
    print(f'Deve se alistar este ano (\033[34m{ano}\033[m)!')
else:
    print(f'Você perdeu o prazo para alistamento, \ndeveria ter se alistado em \033[34m{ano-(ano-nasc)+18}\033[m há \033[34m{18-(ano-nasc)}\033[m ano(s).')
