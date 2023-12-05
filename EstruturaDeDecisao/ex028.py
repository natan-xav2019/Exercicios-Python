# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

import locale
from locale import currency

locale.setlocale(locale.LC_ALL,"pt_BR")

DESCONTO_PRODUTO = 5
PROCENTAGEM_DESCONTO_CARTAO = 0.05

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
    
produtos = [] 
escolhas = []
texto_escolha = ""

produtos.append(Produto("File Duplo", 4.9, 5.8))
produtos.append(Produto("Alcatra", 5.9, 6.8))
produtos.append(Produto("Picanha", 6.9, 7.8))

for produto in produtos:
    escolhas.append(produto.nome)
    texto_escolha += f"{produto.nome}, "

texto_escolha = texto_escolha[:-2]
texto_escolha += "."

posisao_virgula = texto_escolha.rfind(',')

texto_escolha = f"{texto_escolha[:posisao_virgula]} e{texto_escolha[posisao_virgula + 1:]}"

while True:
    escolha = input("Escreva o tipo de carne desejada das opções acima: ")
    if escolha in escolhas:
        break
    else:
        print(f"Escolha uma das {len(escolhas)} opções.")
        print(texto_escolha)


produto_quantidade = float(input(f"Digite a quantidade de {escolha} desejado: "))

while True:
    e_cartao = input(f"Ira pagar com o cartão: ").upper()

    if e_cartao in ["SIM","NÃO"]:
        if(e_cartao == "SIM"):
            e_cartao = True
        elif(e_cartao == "NÃO"):
            e_cartao = False
        break
    else:
        print("digite Sim ou Não apenas.")

for produto in produtos:
    if escolha == produto.nome:
        produto.calcular_preco(produto_quantidade)
        print(f"Tipo: {produto.nome}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Preço total: {currency(produto.pagar)}")
        if(e_cartao):
            desconto = produto.pagar*PROCENTAGEM_DESCONTO_CARTAO
            print(f"tipo de pagamento: cartão promocional")
            print(f"valor do desconto: {currency(desconto)}")
        else:
            desconto = 0
            print(f"tipo de pagamento: Sem cartão promocional")
            print(f"valor do desconto: 0")

        print(f"valor a pagar: {currency(produto.pagar - desconto)}")