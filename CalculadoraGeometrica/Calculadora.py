from Clases import clCuadrado, clCirculo, clRectangulo, clTriangulo

print("Bienvenido - Calculadora Geometrica")
continuar = "s"
while continuar.lower() == "s":
    print("Seleccione la figura a calcular:\n1-Cuadrado\n2-Rectangulo\n3-Triangulo\n4-Circulo\n5-Rombo")
    seleccion = int(input())
    if seleccion == 1:
        cuadrado = clCuadrado.Cuadrado()
        cuadrado.lado = float(input("Ingrese Lado: "))
        print(f'El perimetro del cuadrado es {cuadrado.CalcularPerimetro()}')
        print(f'El área del cuadrado es {cuadrado.CalcularArea()}')

    elif seleccion == 2:
        rectangulo = clRectangulo.Rectangulo()
        rectangulo.base = float(input("Ingrese Base: "))
        rectangulo.altura = float(input("Ingrese Altura: "))
        print(f'El perimetro del rectangulo es {rectangulo.CalcularPerimetro()}')
        print(f'El área del rectangulo es {rectangulo.CalcularArea()}')

    elif seleccion == 3:
        triangulo = clTriangulo.Triangulo()
        triangulo.lado1 = float(input("Ingrese un lado del triángulo: "))
        triangulo.lado2 = float(input("Ingrese otro lado del triángulo: "))
        triangulo.lado3 = float(input("Ingrese el ultimo lado del triángulo: "))
        area = triangulo.CalcularArea()
        if area !=0:
            print(f'El perimetro del triángulo es {triangulo.CalcularPerimetro()}')
            print(f'El área del triángulo es {area}')

    elif seleccion == 4:
        circulo = clCirculo.Circulo()
        circulo.radio = float(input("Ingrese el radio: "))
        print(f'El perimetro del circulo es {circulo.CalcularPerimetro()}')
        print(f'El área del circulo es {circulo.CalcularArea()}')

    elif seleccion == 5:
        rombo = clCuadrado.Rombo()
        rombo.lado = float(input("Ingrese el largo del lado del rombo: "))
        rombo.diagonalMayor = float(input("Ingrese la diagonal mayor: "))
        rombo.diagonalMenor = float(input("Ingrese la diagonal menor: "))
        print(f'El perimetro del rombo es {rombo.CalcularPerimetro()}')
        print(f'El áreadel rombo es {rombo.CalcularArea()}')


    continuar = str(input("Para realizar otra operación presione 'S' o 'N' para salir: "))
