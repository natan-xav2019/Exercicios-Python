# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheitParaCelsius = lambda fahrenheit : 5 * ((fahrenheit-32) / 9)

while True:
    try:
        fahrenheit = float(input("Digite o temperatura fahrenheit para converter para celsius: "))
        break
    except:
        print("Digite apenas numeros")

celsius = fahrenheitParaCelsius(fahrenheit)

print(f"a temperaru de {fahrenheit}° fahrenheit para celsius e de {celsius:.2f}°.")