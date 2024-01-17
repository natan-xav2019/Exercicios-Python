# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

import locale

locale.setlocale(locale.LC_ALL,"PT-br")

produtos:dict[int,tuple(str,float)] = {
    100: ("Cachorro Quente", 1.2),
    101: ("Bauru Simples", 1.3),
    102: ("Bauru com ovoe", 1.5),
    103: ("Hambúrguer", 1.2),
    104: ("Cheeseburguer", 1.3),
    105: ("Refrigerante", 1),
}

itens:list[int,float] = []

valor = 0
repetir = False
continuar = ""

while True:

    while repetir:
        continuar = input(f"Deseja continuar: [s/n]").upper()
        if continuar in ["S","N"]:
            repetir = False
        else:
            print("Digite apenas S ou N.")
        
    if continuar in ["N"]:
        break
    else:
        while True:
            codigo = int(input("Digite o codigo do produto: "))
            if codigo in produtos:
                nome, preso = produtos[codigo]
                quantidade = int(input(f"Quantidade de {nome} pelo preço {locale.currency(preso)}: "))
                valor += quantidade * preso
                itens.append([codigo,quantidade])
                repetir = True
                break
            else:
                print("Digite um codigo valido!!!")
            

for codigo, quantidade in itens:
    nome, preso = produtos[codigo]
    print(f"Produto {nome} com quantidade {quantidade} da: {locale.currency(quantidade * preso)}")
print(f"Valor total {locale.currency(valor)}")