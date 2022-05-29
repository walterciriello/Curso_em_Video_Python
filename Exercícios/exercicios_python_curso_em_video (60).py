s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Estes segmentos podem formar um triâgulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Estes segmentos não podem formar um triângulo!')
