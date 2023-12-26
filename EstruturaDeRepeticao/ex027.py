# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
from statistics import median

quantidade_turma = int(input("Digite a quantidade de turmas : "))

quantidade_aluna = []

for contador in range(1,quantidade_turma+1):
    while True:
        quantidade = int(input(f"Digite a quantidade de alunos turma {contador}: "))

        if 0 <= quantidade <= 40:
            quantidade_aluna.append(quantidade)
            break
        else:
            print("Digite numeros de 0 a 40.")
        
media = median(quantidade_aluna)

print(f"A média de {media:.2f} alunos por turma.")
