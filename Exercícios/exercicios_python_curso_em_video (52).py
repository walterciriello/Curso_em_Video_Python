sal = float(input('Digite o salário atual do funcionário? R$'))
if sal > 1250:
    nsal = sal + (sal * 10 / 100)
else:
    nsal = sal + (sal * 15 / 100)
print('O salário do funcionário após o aumento será de R${:.2f}'.format(nsal))
