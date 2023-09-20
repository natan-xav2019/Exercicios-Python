# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

calculoAreaQuadrado = lambda lado : lado**2

while True:
    try:
        lado = float(input("Digite : "))
        break
    except:
        print("por favor digite um numero")

DobroAreaQuadrado = calculoAreaQuadrado(lado)*2

print(f"Um quadrado de lado igual a {lado} e da area de um quadrado igual vezes 2 igual a {DobroAreaQuadrado}.")