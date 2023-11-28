# Um posto esta vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro.
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (condificado da seguinte forma A-álccol Ggasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se qe o preço do litro da gasolina e R$ 2,50 o preço do litro do álcool e R$ 1,90.

import locale

locale.setlocale(locale.LC_MONETARY,"pt-BR")


class Combustivel:

    def __init__(self,nome: str,preso: float,desconto_ate_20: float,desconto_depois_20: float ) -> None:
        self.nome = nome
        self.preso = preso
        self.desconto_ate_20 = desconto_ate_20
        self.desconto_depois_20 = desconto_depois_20
        self.vendido = 0
        pass

    def status(self) -> None:
        print(f"nome do combustivel: {self.nome}")
        print(f"preço do combustivel por litro: {locale.currency(self.preso)}")
        print(f"desconto ate 20 do combustivel: {self.desconto_ate_20}%")
        print(f"desconto depois 20 do combustivel: {self.desconto_depois_20}%\n")

    def litros_vendido(self,litros: float) -> None:
        if(litros < 20) :
            self.vendido = litros * self.preso * (1 - self.desconto_ate_20/100)
            print(f"O combustivel {self.nome} com {litros} litros vamos ter o desconto de {self.desconto_ate_20}% pelo valor de {locale.currency(self.vendido)}")
        else:
            self.vendido = litros * self.preso * (1 - self.desconto_depois_20/100)
            print(f"O combustivel {self.nome} com {litros} litros vamos ter o desconto de {self.desconto_depois_20}% pelo valor de {locale.currency(self.vendido)}")
        
        
alcool = Combustivel("Álcool", 1.90 , 3, 5)
gasolina = Combustivel("Gasolina", 2.50 , 4, 6)
while True:
    try:
        opcao = input("Escolha o tipo de combustivel G(Gasolina) é A(Álcool): ").upper()
        if(opcao in "G" or opcao in "A"):
            break
        else:
            print("Digite apenas \"G\" ou \"A\" como foi pedido.")
    except:
        print("Digite apenas Letras")

while True:
    try:
        litro = float(input("Digite a quantidade de alcool desejado: "))
        if(litro <= 0):
            print("Apenas Numeros positivos")
        else:
            break
    except:
        print("Digite apenas numeros")

if opcao in "G":
    gasolina.litros_vendido(litro)
elif opcao in "A":
    alcool.litros_vendido(litro)