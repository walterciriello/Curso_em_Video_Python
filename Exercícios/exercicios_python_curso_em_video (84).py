num = cont = soma = 0 # atribuindo valor inicial as variáveis;
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999: # o número 999  neste caso é o flag de saída;
        break # joga a operação para fora do laço;
    cont += 1 # como o contador e a soma estão abaixo do break o número 999 não entra na operação;
    soma += num
print(f'Foram digitados {cont} números e a soma entre eles é {soma}!')
