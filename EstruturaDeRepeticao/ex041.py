# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

import locale

locale.setlocale(locale.LC_ALL,"PT-br")

JUROS_MES:dict[int,float] = { 
    1:0,
    3:0.1,
    6:0.15,
    9:0.2,
    12:0.25,
}

valor = float(input("Digite o valor da compra para  saber as devidas parcelas: "))

print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
for mes,juros in JUROS_MES.items():
    print(f"{locale.currency(valor + valor*juros)}\t{valor*juros}\t\t{mes}\t\t{locale.currency((valor + valor*juros)/mes)}")

