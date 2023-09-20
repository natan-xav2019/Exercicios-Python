# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import locale
import math

class Balde_tinta:
    def __init__(self,litro, preco):
        self.quant_litro = litro
        self.preco = preco

def main():
    locale.setlocale(locale.LC_MONETARY,"pt-BR")

    METRO_QUADRADO_POR_LITRO = 6

    latas = Balde_tinta(18,80)
    galoes = Balde_tinta(3.6,25)

    while True:
        try:
            area_quadrado = float(input("Digite a area em metros do quadrado a ser pintado: "))
            if(area_quadrado > 0):
                break
            print("Digite apenas numeros positivos.")
        except:
            print("Digite apenas numeros")

    area_em_litros = area_quadrado / METRO_QUADRADO_POR_LITRO

    quant_latas_comprar = math.ceil(area_em_litros / latas.quant_litro)
    pagar_latas = quant_latas_comprar * latas.preco

    quant_galoes_comprar = math.ceil(area_em_litros / galoes.quant_litro)
    pagar_galoes = quant_galoes_comprar * galoes.preco

    print(f"\n\tLatas")
    print(f"quantidade: {quant_latas_comprar}")
    print(f"Pagar: {locale.currency(pagar_latas)}\n")
    print(f"\tGalões")
    print(f"quantidade: {quant_galoes_comprar}")
    print(f"Pagar: {locale.currency(pagar_galoes)}\n")

    quant_latas_comprar = 0

    while quant_galoes_comprar > int(galoes.quant_litro) % latas.quant_litro:
        quant_galoes_comprar -= (int(galoes.quant_litro) % latas.quant_litro + 1)
        quant_latas_comprar += 1

    pagar_latas = quant_latas_comprar * latas.preco
    pagar_galoes = quant_galoes_comprar * galoes.preco
    pagar_total = pagar_latas + pagar_galoes

    print(f"\nPagando economizando")
    print(f"quantidade Latas: {quant_latas_comprar}")
    print(f"quantidade Galões: {quant_galoes_comprar}")
    print(f"Pagar: {locale.currency(pagar_total)}\n")
    
if __name__ == "__main__":
    main()