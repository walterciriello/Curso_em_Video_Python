resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maoir valor foi {maior} e o menor valor foi {menor}')
