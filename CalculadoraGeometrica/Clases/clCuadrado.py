from CalculadoraGeometrica.Clases.clTriangulo import Triangulo
from Clases import clFiguraGeometrica as fg

class Cuadrado(fg.FigurasGeometricas):
    def __init__(self):
        self.lado = 0.0
        self.asas = Triangulo
    def CalcularPerimetro(self):
        perimetro = self.lado * 4
        return perimetro
    def CalcularArea(self):
        area = (self.lado) * (self.lado)

        return area

class Rombo(Cuadrado):
    def __init__(self):
        self.diagonalMayor = 0.0
        self.diagonalMenor = 0.0
        super().__init__()
    def CalcularPerimetro(self):
        return super().CalcularPerimetro()
    def CalcularArea(self):
        area = (self.diagonalMayor * self.diagonalMenor)/2
        return area

