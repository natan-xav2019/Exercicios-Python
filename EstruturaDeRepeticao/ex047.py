# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

class Atleta:
    def __init__( self,nome:str,notas:list[float] ) -> None:
        self.nome = nome
        self.notas = list(notas)
        array_calculo_media = list(notas)

        self.maior = max(notas)
        self.menor = min(notas)

        array_calculo_media.remove(self.maior)
        array_calculo_media.remove(self.menor)

        self.media_salto = sum(array_calculo_media)/len(array_calculo_media)

    def status(self):
        contador = 0
        print(f"\nÁtleta: {self.nome}")
        while contador < 5:
            print(f"Nota: {self.notas[contador]:.1f} m")
            contador += 1

        print("\nResultado final:")
        print(f"Atleta: {self.nome}")
        print(f"Melhor Salto: {self.maior:.1f} m")
        print(f"Pior Salto: {self.menor:.1f} m")
        print(f"Média: {self.media_salto:.2f} m")

contador = 0
notas = []
denovo = False

nome = input("Atleta: ")

while contador < 7:
    if denovo:
        notas[contador] = float(input(f"Nota: "))
    else:
        denovo = True
        notas.append(float(input(f"Nota: ")))
    if notas[contador] > 0:
        contador += 1
        denovo = False
    else:
        print(f"Digite apenas numero possitivos.")

atleta = Atleta(nome,notas)
atleta.status()