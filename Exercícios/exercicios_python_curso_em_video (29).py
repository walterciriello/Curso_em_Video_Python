print('-'*40)
print('Exercício nº 15')
print('-'*40)
dia = int(input('Quantos dias durou a locação? '))
km = float(input('Quantos KM o veículo percorreu? '))
cust_dia = dia * 60
cust_km = km * 0.15
#cust_total = cust_dia + cust_km (posso inserir direto em "format" como no exemplo abaixo)
print('O valor total das diárias foi de R${:.2f} \nO valor dos KM rodados foi de R${:.2f}'.format(cust_dia, cust_km))
print('O valor total a ser pago é de R${:.2f}'.format(cust_dia + cust_km))
print('-'*40)
