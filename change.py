def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto= float(input('ingresar el gasto: '))
    recibido= int(input("Ingrese el dinero recibido: " ))

    print('Ingresar gasto: ')
    print(gasto)
    print('Dinero recibido ')
    print(recibido)
    print("")
    print("Vuelto")
    print("")
    pesos=int(recibido - gasto)
    centavos=round(((recibido - gasto) - pesos) * 100 )
    print("Pesos: ")
    print(pesos)
    print("Centavos: ")
    print(centavos)

#change()