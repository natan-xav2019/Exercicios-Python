# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

TAMANHO = 10

def somaDosQuadrados(vetor:list[int]):
    soma = 0
    for numero in vetor:
        soma += numero**2

    return soma

vetor = []
contador = 0

print("Digite 10 numeros")
while contador < TAMANHO:
    try:
        numero = int(input("Digite o numero: "))
        vetor.append(numero)
        contador += 1
    except:
        print("Apenas numeros inteiros.")

resposta = somaDosQuadrados(vetor)

print(f'a soma do quadrado dos numeros colocados é {resposta} .')