# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def fatorial(numero: int) -> int:
    if numero == 1:
        return 1
    elif numero <= 0:
        return False
    else:
        return fatorial(numero-1)*numero

repetir_fatorial = True

while repetir_fatorial:
    repetir = True
    try:
        numero = int(input("Digite um número para saber o fatorial dele: "))
        if numero <= 0:
            print("Não existe fatorial de numero negativo!!!")
        elif numero > 16:
            print("Apenas numeros menores que igual a 16.")
        else:
            print(f"{numero}! = {fatorial(numero)}")
            print("gostaria de continuar?")
            while repetir:
                continuar = input("Digite S ou N: ").upper()
                if(continuar == 'N' ):
                    repetir = False
                    repetir_fatorial = False
                elif(continuar == 'S' ):
                    print("Vamos fazer o fatorial novamente!!")
                    repetir = False
                else:
                    print("Apenas S ou N.")
    except:
        print("Digite apenas números.")

