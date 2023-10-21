# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

def calculoDelta(a,b,c):
    return b**2 -4*a*c

def calculoBaskara(a,b,c):
    delta = calculoDelta(a,b,c)
    x = []
    if delta > 0 :
        x.append( (-b + math.sqrt(delta))/(2*a) )
        x.append( (-b - math.sqrt(delta))/(2*a) )
    elif delta == 0 :
        x.append( (-b + delta)/(2*a) )
    else:
        return None

    return x

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

raizes = calculoBaskara(a,b,c)
if raizes is not None:
    if len(raizes) == 2:
        print(f"Possui duas raizes {raizes[0]} e {raizes[1]}")
    else:
        print(f"Possui uma raiz {raizes[0]}")
else:
    print(f"não possui raiz")
    
