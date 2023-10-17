# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um numero: "))

if(numero == 0):
    print("O numero 0 não existe positivo e negativo somente 0.")
else:
    numero = abs(numero)
    print(f"O numero positivo e { str(numero).replace('.', ',') }.")
    print(f"O numero negativo e { str(numero*-1).replace('.', ',')}.")