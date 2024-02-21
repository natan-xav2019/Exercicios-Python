# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

TAMANHO = 5

def operasaoVetor(vetor:list[int]):
    soma = 0
    multiplicasao = 1
    for contador in range(0,TAMANHO):
        soma += vetor[contador]
        multiplicasao *= vetor[contador]

    print(f'Soma: {soma}')
    print(f'multiplicação: {multiplicasao}')
    print(f'Valores {vetor}')

contador = 0
vetor = []
primeira = True

print("Digite 5 numeros.")
while contador < TAMANHO:
    try:
        numero = int(input("Digite o numero: "))
        vetor.append(numero)
        contador += 1
    except:
        print("Apenas numeros inteiros.")

operasaoVetor(vetor)