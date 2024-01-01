# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

from statistics import median

class Pessoa:
    def __init__(self,codigo: int,altura: float,peso: float) -> None:
        self.codigo = codigo
        self.altura = altura
        self.peso = peso
        self.MMC = self.calculoMMC()
        pass

    def calculoMMC(self):
        return self.peso/(self.altura**2)


pessoas: list[Pessoa] = []
pessoa_mais_alta = 0
pessoa_mais_baixa = 0
pessoa_mais_gorda = 0
pessoa_mais_magra = 0

print("Academia com sendo deseja saber quem são os clientes mais altos, baixos, magros e gordos.")
print("Por favor informe abaixo o codigo da pessoa, altura e peso")
while True:

    codigo = int(input(f"Codigo da pessoa: "))

    if codigo == 0:
        break
    else:
        igual = False
        for pessoa in pessoas:
            if pessoa.codigo == codigo:
                igual = True
                break
            
        if not igual:
            altura = float(input(f"Altura em metros: "))
            peso = float(input(f"Peso em kg: "))
            
            pessoa = Pessoa(codigo,altura,peso)
            pessoas.append(pessoa)

        else:
            print("O codigo de cada pessoa precisa ser unico")

for index,pessoa in enumerate(pessoas):
    if pessoa.altura >= pessoas[pessoa_mais_alta].altura:
        pessoa_mais_alta = index
    if pessoa.altura <= pessoas[pessoa_mais_baixa].altura:
        pessoa_mais_baixa = index
    if pessoa.MMC >= pessoas[pessoa_mais_gorda].MMC:
        pessoa_mais_gorda = index
    if pessoa.MMC <= pessoas[pessoa_mais_magra].MMC:
        pessoa_mais_magra = index

print("\nA pessoa mais alta:")
print(f"Codigo: {pessoas[pessoa_mais_alta].codigo}")
print(f"Altura: {pessoas[pessoa_mais_alta].altura}")
print(f"Peso: {pessoas[pessoa_mais_alta].peso}\n")

print("A pessoa mais baixa:")
print(f"Codigo: {pessoas[pessoa_mais_baixa].codigo}")
print(f"Altura: {pessoas[pessoa_mais_baixa].altura}")
print(f"Peso: {pessoas[pessoa_mais_baixa].peso}\n")

print("A pessoa mais gordo:")
print(f"Codigo: {pessoas[pessoa_mais_gorda].codigo}")
print(f"Altura: {pessoas[pessoa_mais_gorda].altura}")
print(f"Peso: {pessoas[pessoa_mais_gorda].peso}\n")

print("A pessoa mais magra:")
print(f"Codigo: {pessoas[pessoa_mais_magra].codigo}")
print(f"Altura: {pessoas[pessoa_mais_magra].altura}")
print(f"Peso: {pessoas[pessoa_mais_magra].peso}\n")

media_alturas = median([pessoa.altura for pessoa in pessoas ])
media_peso = median([pessoa.peso for pessoa in pessoas ])

print(f"Media Alturas: {media_alturas}")
print(f"Media Pesos: {media_peso}")