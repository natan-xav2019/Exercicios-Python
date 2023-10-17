# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

class Triangulo:
    def __init__(self, lados=[0,0,0]):
        self.__A = lados[0]
        self.__B = lados[1]
        self.__C = lados[2]
        self.eTriangulo = self.isTriangulo()
        pass

    def isTriangulo(self) -> bool:
        if self.__A + self.__B <= self.__C or self.__A + self.__C <= self.__B or self.__B + self.__C <= self.__A:
            return True
        else:
            return False
        
    def tipoTriangulo(self) -> str:
        if(self.__A == self.__B or self.__A == self.__C):
            return "Equilátero"
        
        if( (self.__A == self.__B and self.__A != self.__C) or (self.__B == self.__C or self.__A != self.__C) or (self.__A == self.__C or self.__A != self.__B) ):
            return "Isósceles"

        if(self.__A != self.__B and self.__A != self.__C and self.__B != self.__C):
            return "Escaleno"

    def __str__(self) -> str:
        text = f"Triângulo com lados a = {self.__A}, b = {self.__B}, c = {self.__C}.\n"

        if(self.eTriangulo):
            text = text + f"Esses numeros formão um triângulo.\n"
        else:
            text = text + f"Esses numeros Não formão um triângulo.\n"
        
        return text

# Exemplos de uso

lados = [6,8,10]

t2 = Triangulo(lados)
print(t2)

        