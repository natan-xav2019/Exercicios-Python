# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
import locale

locale.setlocale(locale.LC_ALL,"pt_BR")

DESCONTO_PRODUTO = 5
DESCONTO_PRESO = 25
DESCONTO_QUANTIDADE = 8
VALOR_DESCONTADO = 0.9

class Produto:

    def __init__(self,nome:str, preso_normal:float, preso_acima:float, quantidade=None) -> None:
        self.nome = nome
        self.preso_normal = preso_normal
        self.preso_acima = preso_acima
        
        if not quantidade == None:
            self.quantidade = quantidade
            self.pagar = self.calcular_preco(self.quantidade)
        else:
            self.quantidade = 0
            self.pagar = 0
        pass

    def calcular_preco(self, quantidade=None):
        if not quantidade == None:
            self.quantidade = quantidade

        if self.quantidade < DESCONTO_PRODUTO:
            self.pagar = self.quantidade * self.preso_normal
        elif self.quantidade >= DESCONTO_PRODUTO:
            self.pagar = self.quantidade * self.preso_acima

        return self.pagar

morango = Produto( "Morango", 2.5 , 2.2 )
masa = Produto( "Maçã", 1.8 , 1.5 )

morango.quantidade = float(input("Digite a quantidade de morangos comprados: "))

masa.quantidade = float(input("Digite a quantidade de maça comprados: "))

morango.calcular_preco(morango.quantidade)
masa.calcular_preco(masa.quantidade)

total_preso = morango.pagar + masa.pagar
total_quantidade = morango.quantidade + masa.quantidade

if total_preso >= DESCONTO_PRESO or total_quantidade > DESCONTO_QUANTIDADE:
    total_preso *= VALOR_DESCONTADO

print(f"Valor a ser pago pelo cliente: {locale.currency(total_preso)}")

