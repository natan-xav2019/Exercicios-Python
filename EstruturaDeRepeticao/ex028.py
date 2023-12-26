# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
from statistics import median
import locale

locale.setlocale(locale.LC_ALL,"pt_BR")

quantidade_CD = int(input("Digite a quantidade de turmas : "))

valor_CD = []

for contador in range(1,quantidade_CD+1):
    valor_CD.append(int(input(f"Digite a valor do CD {contador}: ")))
        
total = sum(valor_CD)
media = median(valor_CD)

print(f"\nQuantidade de CDs {len(valor_CD)}")

for index,valor in enumerate(valor_CD):
    print(f"CD {index+1} custa: {locale.currency(valor)}")

print(f"valor de todos os CDs {locale.currency(total)}")
print(f"valor médio CDs {locale.currency(media)}")
