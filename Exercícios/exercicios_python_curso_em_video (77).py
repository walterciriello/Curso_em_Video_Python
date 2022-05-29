from time import sleep
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print('''ESCOLHA UMA OPÇÃO:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('SUA OPÇÃO: '))
    if opcao == 1:
        print(f'A soma entre os valores é: \033[34m{v1 + v2}\033[m')
    elif opcao == 2:
        print(f'A multiplicação entre os valores é: \033[34m{v1 * v2}\033[m')
    elif opcao == 3:
        if v1 > v2:
            print(f'O maior valor é: \033[34m{v1}\033[m')
        elif v2 > v1:
            print(f'O maior valor é: \033[34m{v2}\033[m')
        else:
            print('Os valores são \033[34miguais\033[m.')
    elif opcao == 4:
        print('\033[34mESCOLHA OS NOVOS VALORES:\033[m')
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
sleep(2)
print('Fim')
