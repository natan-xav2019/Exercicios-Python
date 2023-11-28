# Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou impar;
# b. positivo ou negativo;
# c. inteiro ou decimal;

def par_ou_impar(numero: float)-> None:
    if numero % 2 == 0:
        print(f"O numero {numero} é par.")
    else:
        print(f"O numero {numero} é Impar.")

def positivo_ou_negativo(numero: float)-> None:
    if numero >= 0:
        print(f"O numero {numero} é positivo.")
    else:
        print(f"O numero {numero} é negativo.")

def inteiro_ou_decimal(numero: float)-> None:
    if numero == round(numero):
        print(f"O numero {numero} é inteiro.")
    else :
        print(f"O numero {numero} é decimal.")

numeros = []

numeros.append( float(input("Digite o primeiro numero: ")))
numeros.append( float(input("Digite o Segundo numero: ")))

print("Os comandos so podem ser A, B, C.\n")

comando = input("digite o comando: ")
comando = comando.upper()

for numero in numeros:
    if comando in "A":
        par_ou_impar(numero)
    elif comando in "B":
        positivo_ou_negativo(numero)
    elif comando in "C":
        inteiro_ou_decimal(numero)