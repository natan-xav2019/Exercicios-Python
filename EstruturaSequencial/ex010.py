# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsiusParaFahrenheit = lambda celsius : 1.8 * celsius + 32

while True:
    try:
        celsius = float(input("Digite o temperatura celsius para converter para celsius: "))
        break
    except:
        print("Digite apenas numeros")

fahrenheit = celsiusParaFahrenheit(celsius)

print(f"a temperaru de {celsius}° celsius para fahrenheit e de {fahrenheit:.2f}°.")