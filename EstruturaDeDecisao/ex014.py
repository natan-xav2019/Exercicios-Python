# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

from statistics import mean

def conceito_media(media):
    if( media <= 10  and media >= 9 ):
        return "A"
    elif( media < 9  and media >= 7.5 ):
        return "B"
    elif( media < 7.5  and media >= 6 ):
        return "C"
    elif( media < 6  and media >= 4 ):
        return "D"
    elif( media < 4  and media >= 0 ):
        return "E"


notas = []

for i in range(2):
    primeira_tentativa = True
    while True:
        try:
            if( primeira_tentativa ):
                notas.append(float(input(f"A nota {i+1}: ")))
                primeira_tentativa = False
            else:
                notas[i] = float(input(f"A nota {i+1} de novo: "))

            if(notas[i] <= 10 and notas[i] >= 0):
                break
            else:
                print("Digite apenas numeros de 0 a 10.")
        except:
            print("Digite apenas numeros")

media = mean(notas)
conceito = (conceito_media(media))

print("-" * 15)

i=1

for nota in notas:
    print(f"nota {i}: {nota}")
    i+=1

print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if(conceito == "A" or conceito == "B" or conceito == "C"):
    print("APROVADO")
elif(conceito == "D" or conceito == "E"):
    print("REPROVADO")


