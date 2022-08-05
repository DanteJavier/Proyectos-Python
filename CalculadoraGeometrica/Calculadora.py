from Clases import clCuadrado, clCirculo, clRectangulo, clTriangulo

print("Bienvenido - Calculadora Geometrica")
print("Seleccione la figura a calcular:\n1-Cuadrado\n2-Rectangulo\n3-Triangulo\n4-Circulo")
seleccion = int(input())
continuar = "s"
while continuar.lower() == "s":
    if seleccion == 1:
        cuadrado = clCuadrado.Cuadrado()
        cuadrado.lado = float(input("Ingrese Lado: "))
        print(cuadrado.CalcularPerimetro())
        print(cuadrado.CalcularArea())


    if seleccion == 2:
        rectangulo = clRectangulo.Rectangulo()
        rectangulo.base = float(input("Ingrese Base: "))
        rectangulo.altura = float(input("Ingrese Altura: "))
        print(rectangulo.CalcularPerimetro())
        print(rectangulo.CalcularArea())

    if seleccion == 3:

    continuar = str(input("Para realizar otra operación presione 'S' o 'N' para salir: "))
