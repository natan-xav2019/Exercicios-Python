# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

pasou = True
contador = 0

while True:
    try:
        quantidade_numeros = int(input("Digite a quantidade de numeros desejados: "))
        if quantidade_numeros > 0:
            break
        else:
            print("Digite apenas numeros positivos.")
    except:
        print("Digite apenas números.")

while contador < quantidade_numeros:
    numeros.append(float(input(f"Digite o numero {contador + 1}: ")))
    contador += 1

print(f"numeros: {numeros}")
print(f"maior: {max(numeros)}")
print(f"menor: {min(numeros)}")
print(f"soma: {sum(numeros)}")
