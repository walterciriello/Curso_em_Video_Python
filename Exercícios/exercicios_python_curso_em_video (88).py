total = caro = barato = cont = 0
maisbarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < barato:
        barato = preco
        maisbarato = produto
    resp = ' '
    while resp not in 'SN':
       resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de: R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {maisbarato} que custa R$ {barato:.2f}')
