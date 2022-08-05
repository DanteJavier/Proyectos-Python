import clFiguraGeometrica as fg

class Rectangulo(fg.FigurasGeometricas):
    def __init__(self):
        self.base = 0.0
        self.altura = 0.0
    def CalcularPerimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro
    def CalcularArea(self):
        area = self.base * self.altura
        return area 