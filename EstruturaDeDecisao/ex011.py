# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

import locale

locale.setlocale(locale.LC_MONETARY,"pt-BR")

percentual = 0

calculo_bonus = lambda salario,percentual : salario * percentual

while True:
    try:
        salario = float(input("Digite o salario para calcular o reajuste: "))
        if(salario > 0):
            break
    except:
        print("Digite apenas numeros.")

if(salario <= 280):
    percentual = 0.2
elif(salario > 280 and salario <= 700):
    percentual = 0.15
elif(salario > 700 and salario <= 1500):
    percentual = 0.1
else:
    percentual = 0.05

reajusto = calculo_bonus(salario, percentual)
novo_salario = salario + reajusto

print(f"Salário: {locale.currency(salario)}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"O valor do aumento: {locale.currency(reajusto)}")
print(f"O novo salário: {locale.currency(novo_salario)}")