# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def apresentarMediaAlunos(medias:list[float]):
    for aluno,media in enumerate(medias):
        if media > 7:
            print(f'Aluno {aluno+1} com media {media} maior que 7.0.')

REPETISAO = 10
contador = 0
medias = []
soma = 0
quant_notas = contador

while contador < REPETISAO:
    while quant_notas < 4:
        nota = float(input(f'Digite a nota { quant_notas + 1 }: '))
        if 0 <= nota <= 10:
            soma += nota
            quant_notas += 1
        else:
            print("Digite notas entre 0 é 10.")
    
    quant_notas = 0
    medias.append( soma / 4 )
    soma = 0
    contador += 1

apresentarMediaAlunos(medias)


