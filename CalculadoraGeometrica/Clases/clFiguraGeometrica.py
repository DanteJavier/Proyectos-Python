import math

class FigurasGeometricas():
    def CalcularPerimetro():
        pass
    def CalcularArea():
        pass
    
class Cuadrado(FigurasGeometricas):
    def __init__(self,_lado = 0):
        self.lado = _lado
    def CalcularPerimetro(self):
        perimetro = self.lado * 4
        return perimetro
    def CalularArea(self):
        area = self.lado * self.lado
        return area

class Rectangulo(FigurasGeometricas):
    def __init__(self,_base = 0,_altura = 0):
        self.base = _base
        self.altura = _altura
    def CalcularPerimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro
    def CalcularArea(self):
        area = self.base * self.altura
        return area   

class Circulo(FigurasGeometricas):
    def __init__(self,_radio = 0):
        self.radio = _radio
    def CalcularPerimetro(self):
        perimetro = math.pi * self.radio
        return perimetro
    def CalcularArea(self):
        area = math.pi * (self.radio**2)
        return area

class Triangulo(FigurasGeometricas):
    def __init__(self,_lado1 = 0 ,_lado2 = 0 ,_lado3 = 0):
        self.lado1 = _lado1
        self.lado2 = _lado2
        self.lado3 = _lado3
    def CalcularPerimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro
    def CalcularArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        return area
        