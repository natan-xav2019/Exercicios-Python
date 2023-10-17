# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
import statistics

NOTA_MEDIA = 7
QUANT_NOTAS = 2

notas = []

for i in range( QUANT_NOTAS ):
    notas.append(float(input(f"Digite a nota {i+1}: ")))

media = statistics.mean(notas)

print(f"A média é {media:.2f}.")

if(media == 10):
    print("Aprovado com Distinção")
elif(media >= 7):
    print("Aprovado")
else:
    print("Reprovado")
