# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

import locale

locale.setlocale(locale.LC_ALL,"pt_BR")

valor_produto = float(input("Preço do pão: R$ "))
QUANTIDADE_PRODUTOS = 50

print("Panificadora Pão de Ontem - Tabela de preços")

for contador in range(1,QUANTIDADE_PRODUTOS + 1):
    
    preso = valor_produto * contador

    print(f"{contador:2d} - {locale.currency(preso)}")