# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

alunos:list[int,int] = []

contador = 1

while contador < 11:
    igual = False
    id_aluno = int(input("Digite o codigo do aluno: "))
    for aluno in alunos:
        if id_aluno == aluno[0]:
            igual = True
        else:
            igual  = False
    
    if not igual:
        altura_aluno = float(input("Digite a altura: "))
        
        alunos.append([id_aluno,altura_aluno])
        contador += 1
    
id_menor = 0
id_maior = 0

for index,aluno in enumerate(alunos):
    if aluno[0] < alunos[id_menor][0]:
        id_menor = index
    if aluno[1] > alunos[id_maior][1]:
        id_maior = index

print(f"\tMenor")
print(f"Codigo: {alunos[id_menor][0]}")
print(f"Altura: {alunos[id_menor][1]}")

print(f"\tMaior")
print(f"Codigo: {alunos[id_maior][0]}")
print(f"Altura: {alunos[id_maior][1]}")
