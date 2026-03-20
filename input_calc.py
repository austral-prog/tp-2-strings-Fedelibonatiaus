def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base= int(input("base: "))
    altura= int(input("altura: "))
    area= (base * altura)
    perimetro= ((2 * base) + (2 * altura))
    print("Base: " + str(base))
    print("Altura: "  + str(altura))
    print("Area: " + str(area))
    print("Perimetro: " + str(perimetro))

#rectangle()
