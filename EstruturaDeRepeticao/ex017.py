# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial(numero: int) -> int:
    if numero == 1:
        return 1
    elif numero <= 0:
        return False
    else:
        return fatorial(numero-1)*numero
    
while True:
    try:
        numero = int(input("Digite um número para saber o fatorial dele: "))
        if numero <= 0:
            print("Não existe fatorial de numero negativo!!!")
        else:
            break
    except:
        print("Digite apenas números.")

print(f"{numero}! = {fatorial(numero)}")