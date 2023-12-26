# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
from statistics import median

quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))
idades = []

for pessoa in range(1,quantidade_pessoas + 1):
    idades.append(float(input(f"Digite a idade da {pessoa}° pessoa: ")))

media_idade = median(idades)

if 0 <= media_idade <= 25:
    print("A turma é jovem.")
elif 25 < media_idade < 60:
    print("A turma é Adulta.")
elif media_idade >= 60:
    print("A turma é Idosa.")