from tkinter.constants import CASCADE


def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio= int(input("Precio: "))
    descuento= float(input("descuento: "))
    cantidad= int(input("cantidad: "))
    total= (precio - descuento) * cantidad
    print("Precio: " + str(precio))
    print("Descuento: " + str(descuento))
    print("Precio con descuento: " + str(precio - descuento))
    print("Total: " + " " + str(total))


#casting()