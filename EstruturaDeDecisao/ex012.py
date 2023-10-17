# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

import locale

locale.setlocale(locale.LC_MONETARY,"pt-BR")

PERCENTUAL_SINDICADO = 0.03
PERCENTUAL_FGTS = 0.11

while True:
    try:
        ganho_hora = float(input("Digite seu ganho hora: "))
        if(ganho_hora > 0):
            break
    except:
        print("Digite apenas numeros.")

while True:
    try:
        hora_trabalhada_mes = int(input("Digite quantas horas vc trabalha no mes: "))
        if(hora_trabalhada_mes > 0):
            break
    except:
        print("Digite apenas numeros.")

salario_bruto = ganho_hora * hora_trabalhada_mes

if(salario_bruto <= 900):
    percentual = 0
elif(salario_bruto <= 1500):
    percentual = 0.05
elif(salario_bruto <= 2500):
    percentual = 0.1
else:
    percentual = 0.2

ir = percentual * salario_bruto
fgts = PERCENTUAL_FGTS * salario_bruto
sindicado = PERCENTUAL_SINDICADO * salario_bruto

desconto_total = ir + sindicado

salario_liquido = salario_bruto - desconto_total

print(f"\nSalário Bruto: ({ganho_hora} * {hora_trabalhada_mes})\t: {locale.currency(salario_bruto)}")
print(f"(-) IR ({int(percentual*100)}%) \t\t\t: {locale.currency(ir)}")
print(f"INSS ({int(PERCENTUAL_SINDICADO*100)}%) \t\t\t: {locale.currency(sindicado)}")
print(f"FGTS ({int(PERCENTUAL_FGTS*100)}%) \t\t\t: {locale.currency(fgts)}")
print(f"Total de descontos \t\t: {locale.currency(desconto_total)}")
print(f"Salário Liquido \t\t: {locale.currency(salario_liquido)}")