# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

import locale

locale.setlocale(locale.LC_ALL,"PT-br")

ANO_INICIAL = 1995
salario = float(input(f"Digite um salário inicial: "))
AUMENTO = 0.015

for i in range(0,3):
    print(f"Ano {ANO_INICIAL+i} com ajuste {AUMENTO*100*i}% = { locale.currency( salario * (1+AUMENTO*i) )}")
