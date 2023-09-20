# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
import math
import locale

def main():
    PESO_EXEDENTE = 50
    VALOR_MULTA = 4

    locale.setlocale(locale.LC_MONETARY, "pt-BR")

    while True:
        try:
            peso_peixe_float = float(input("Digite o peso do peixe: "))
            if(peso_peixe_float > 0):
                break
            else:
                print("Não existe peso negativo")
        except:
            print("Digite apenas numeros")

    peso_peixe_int = math.floor(peso_peixe_float)

    diferensa = peso_peixe_int - PESO_EXEDENTE

    multa = VALOR_MULTA * diferensa

    if(multa):
        print(f"Deve pagar a multa de {locale.currency(multa)}.")
    else:
        print(f"Não tem multa! um lindo peixe de {peso_peixe_float}Kg.")

if __name__ == "__main__":
    main()