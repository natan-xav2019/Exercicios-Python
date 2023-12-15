# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def E_primo(numero: int) ->bool:
    quantidade_divisores = 0

    for contador in range(1, numero+1 ):
        if numero % contador == 0:
            quantidade_divisores += 1

        if(quantidade_divisores  > 2):
            return False

    return True


while True:
    try:
        numero = int(input("Digite um número para saber se ele e par ou impar: "))
        if numero <= 0:
            print("Numeros primos não podem ser negativos nem 0!!!")
        else:
            break
    except:
        print("Digite apenas numeros.")

if(E_primo(numero)):
    print(f"O número {numero} e Primo.")
else:
    print(f"O número {numero} não e Primo.")