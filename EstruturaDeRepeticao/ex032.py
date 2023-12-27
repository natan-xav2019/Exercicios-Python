# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

def fatorial(numero: int) -> int:
    if(numero != 1):
        print(f"{numero} . ",end="")
    else:
        print(f"{numero} ", end="")

    if numero == 1:
        return 1
    elif numero <= 0:
        return False
    else:
        return fatorial(numero-1)*numero
    
numero = int(input("Fatorial de: "))

print(f"{numero}! = ",end="")
print(f"= {fatorial(numero)}")