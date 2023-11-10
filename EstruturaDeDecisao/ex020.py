# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
from statistics import mean

QUANTIDADE_NOTAS = 3

notas = []

for index in range(QUANTIDADE_NOTAS):
    correta_nota = True
    while True:
        try:
            if(correta_nota):
                notas.append(float(input(f"Digite a nota {index+1}: ")))
            else:
                notas[index] = float(input(f"Digite a nota {index+1}: "))

            if(0 <= notas[index] <= 10):
                break
            else:
                correta_nota = False
        except:
            print("Digite apenas numeros.")

media = mean(notas)

if media == 10:
    print(f"Aprovado com Distinção com media {media}.")
elif media < 7:
    print(f"Reprovado com media {media:.2f}.")
else:
    print(f"Aprovado com media {media:.2f}.")