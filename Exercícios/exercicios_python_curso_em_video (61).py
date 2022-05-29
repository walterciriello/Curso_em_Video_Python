peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/altura**2
print(f'Seu IMC atual é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
