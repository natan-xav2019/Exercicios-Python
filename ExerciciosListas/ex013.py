# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

from statistics import mean

meses_do_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperaturas = []

for mes in meses_do_ano:
    try:
        temperatura = float(input(f"Digite a temperatura media de {mes}: "))
        temperaturas.append(temperatura)
    except:
        print("Digite apenas numeros.")

temperatura_media = mean(temperaturas)

for index,mes in enumerate(meses_do_ano):
    if temperaturas[index] > temperatura_media:
        print(f"O mes de {mes} teve uma temperatura acima da média. com temperadura de {temperaturas[index]:.1f}°C")

