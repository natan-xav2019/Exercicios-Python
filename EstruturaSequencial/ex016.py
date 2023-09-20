# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import locale
import math

class Balde_tinta:
    def __init__(self,litro, preco):
        self.quant_litro = litro
        self.preco = preco

def main():
    locale.setlocale(locale.LC_MONETARY,"pt-BR")

    METRO_QUADRADO_POR_LITRO = 3

    balde = Balde_tinta(18,80)

    while True:
        try:
            area_quadrado = float(input("Digite a area em metros do quadrado a ser pintado: "))
            if(area_quadrado > 0):
                break
            print("Digite apenas numeros positivos.")
        except:
            print("Digite apenas numeros")

    area_em_litros = area_quadrado / METRO_QUADRADO_POR_LITRO
    quant_latas_comprar = math.ceil(area_em_litros / balde.quant_litro)
    pagar = quant_latas_comprar * balde.preco

    print(f"precisa comprar: {quant_latas_comprar}")
    print(f"devera gastar {locale.currency(pagar)}")

if __name__ == "__main__":
    main()