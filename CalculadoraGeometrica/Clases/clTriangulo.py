from Clases import clFiguraGeometrica as fg
import math

class Triangulo(fg.FigurasGeometricas):
    def __init__(self,_lado1 = 0 ,_lado2 = 0 ,_lado3 = 0):
        self.lado1 = _lado1
        self.lado2 = _lado2
        self.lado3 = _lado3
    def CalcularPerimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro
    def CalcularArea(self):
        try:
            s = (self.lado1 + self.lado2 + self.lado3) / 2
            area = math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))
        except:
            print("El triángulo no existe")
            area = 0
        return area
