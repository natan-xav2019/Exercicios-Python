# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

while True:
    try:
        numero = input("Digite um numero inteiro positivo: ")
        if int(numero) > 0:
            break
        else:
            print("Digite numeros positivos")
    except:
        print("Digite apenas numeros")


numero_invertido = numero[::-1]

print(f"Número: {numero}")
print(f"Número invertido: {numero_invertido}")