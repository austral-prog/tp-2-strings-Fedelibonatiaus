
def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    Nombre =input('Ingrese su nombre: ')
    Apellido= input('Ingrese su apellido: ')
    nombre_apellido= (Nombre + " " + Apellido)
    print((nombre_apellido).lower())
    print((nombre_apellido).title())
    print((nombre_apellido).upper())
    print("\t" + (nombre_apellido).lower())

#names()


