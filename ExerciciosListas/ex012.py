# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

from statistics import mean

MAX = 30

def quantidade_Alunos_13anos_Mais_Altura_Acima_Media(idades:list[int],alturas:list[float]):
    contador = 0
    alturas_media = mean(alturas)
    quantosAlunos = 0

    while contador < MAX:
        if idades[contador] < 13 and alturas[contador] < alturas_media:
            quantosAlunos += 1
        contador += 1

    return quantosAlunos
        

idades = []
alturas = []
contador = 0

while contador < MAX:
    try:
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        idades.append(idade)
        alturas.append(altura)
        contador += 1 
    except:
        print("Para idade digite apenas numeros inteiros para altura apenas numeros.")

resposta = quantidade_Alunos_13anos_Mais_Altura_Acima_Media(idades,alturas)

print(f"Quantidade de Alunos: {resposta}")