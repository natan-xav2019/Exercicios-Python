# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numeros = []

pasou = True
contador = 0

while True:
    try:
        quantidade_numeros = int(input("Digite a quantidade de numeros desejados: "))
        if quantidade_numeros > 0:
            break
        else:
            print("Digite apenas numeros positivos.")
    except:
        print("Digite apenas números.")

while contador < quantidade_numeros:
    numero = float(input(f"Digite o numero {contador + 1}: "))
    if(0 <= numero <= 1000):
        numeros.append(numero)
        contador += 1
    else:
        print("Digite apenas numeros entre 0 e 1000.")    
    

print(f"numeros: {numeros}")
print(f"maior: {max(numeros)}")
print(f"menor: {min(numeros)}")
print(f"soma: {sum(numeros)}")
