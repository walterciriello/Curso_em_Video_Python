nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
if media < 5.0:
    print(f'Média: {media:.1f} *REPROVADO*')
elif 7 > media >= 5:
    print(f'Média: {media:.1f} *RECUPERAÇÃO')
else:
    print(f'Média {media:.1f} *APROVADO*')
