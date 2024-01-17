# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

entrada:int = 0
repetir:bool = True
resposta:list[int] = []

while repetir:
    entrada = int(input("Digite um numero inteiro: "))

    if(entrada < 0):
        repetir = False
    else:
        resposta.append(entrada)


for valor in resposta:

    if 0 <= valor <= 25:
        print(f"O valor {valor} esta no quadrante [0-25]")
    elif 26 <= valor <= 50:
        print(f"O valor {valor} esta no quadrante [26-50]")
    elif 51 <= valor <= 75:
        print(f"O valor {valor} esta no quadrante [51-75]")
    elif 76 <= valor <= 100:
        print(f"O valor {valor} esta no quadrante [76-100]")
