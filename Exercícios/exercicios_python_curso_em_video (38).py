#Sorteando a ordem de apresentação dos alunos

import random

numero_de_alunos = int(input("Quantos alunos irão apresentar o trabalho?\n"))
alunos = []

for aluno in range(0, numero_de_alunos):
    alunos.append(str(input("Digite o nome do aluno: ")))

random.shuffle(alunos)

print(f"A ordem de apresentação será {alunos}")
