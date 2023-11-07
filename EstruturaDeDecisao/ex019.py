# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numeros = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 , 16]

LEITURA_MAXIMA = 1000


for index ,numero in enumerate(numeros):
    resto = 1
    if numero < LEITURA_MAXIMA :
        numero_texto = str(numero)
        numero_por_extenso = ""
        for index ,letra in enumerate(numero_texto):
            print(f"{letra} e maior que 1? {1 < int(letra)}")
            if 1 < int(letra):
                plural = True
            else:
                plural = False
            print(f"index: {index}")
            if len(numero_texto) == 3:
                if(index == 0):
                    numero_por_extenso = f"{numero_por_extenso}{letra} centena"
                    if(plural):
                        numero_por_extenso = f"{numero_por_extenso}s, "
                    else:
                        numero_por_extenso =f"{numero_por_extenso} "
                elif(index == 1):
                    numero_por_extenso = f"{numero_por_extenso}{letra} dezena"
                    if(plural):
                        numero_por_extenso = f"{numero_por_extenso}s e"
                    else:
                        numero_por_extenso =f"{numero_por_extenso} e "
                elif(index == 2):
                    numero_por_extenso = f"{numero_por_extenso}{letra} unidade"
                    if(plural):
                        numero_por_extenso = f"{numero_por_extenso}s."
            print(numero_por_extenso)

            # elif len(numero_texto) == 2:
            #     numero_por_extenso = f"{letra} dezena"
            #     if(plural):
            #         numero_por_extenso += "s"

            # else len(numero_texto) == 1:
            #         numero_por_extenso = f"{letra} unidade"
            #     if(plural):
            #         numero_por_extenso += "s."
        
    else:
        print(f"O numero e precisa ser menor que 1000 e maior que -1000")


