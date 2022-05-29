dis = float(input('Digite a distância da viagem: '))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
# preço = dis * 50 if dis <= 200 else dis * 0.45 (alternativa para a resolução acima)
print('O preço da passagem é de R${:.2f}'.format(preço))
