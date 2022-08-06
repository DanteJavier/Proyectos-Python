from Clases import clFiguraGeometrica as fg
import math

class Circulo(fg.FigurasGeometricas):
    def __init__(self):
        self.radio = 0
    def CalcularPerimetro(self):
        perimetro = math.pi * self.radio
        return perimetro
    def CalcularArea(self):
        area = math.pi * (self.radio**2)
        return area