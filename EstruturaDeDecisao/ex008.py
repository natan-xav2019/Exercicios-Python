#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
import locale

locale.setlocale(locale.LC_MONETARY,"pt-BR")

class Produto:
    def __init__(self) -> None:
        self.__nome = ""
        self.__preso = 0

    def get_nome(self) -> str:
        return self.__nome
    
    def get_preso(self) -> float:
        return self.__preso
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_preso(self,preso: float) -> None:
        self.__preso = preso


produtos = []

for i in range(3):
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preso = float(input("Digite o preço: "))
            if(preso <= 0):
                print("Digite apenas valores positivos.")
            else:
                break
        except:
            print("Digite apenas numeros")

    produto = Produto()
    produto.set_nome(nome)
    produto.set_preso(preso)
    
    produtos.append(produto)


menor = 0

for index, produto in enumerate(produtos):
    if( index == 0 ):
        menor = produto.get_preso()
        index_menor = [index]
    elif( menor > produto.get_preso() ):
        menor = produto.get_preso()
        index_menor = [index]
    elif( menor == produto.get_preso() ):
         index_menor.append(index)


print("Preço(s) mais barato(s).")
for index in index_menor:
    print(f"O nome: {produtos[index].get_nome()}")
    print(f"O peço: {produtos[index].get_preso()}")
