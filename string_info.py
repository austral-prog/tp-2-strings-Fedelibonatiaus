def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print("Palabra: " + (palabra))
    print("Longitud: "+ str(len(palabra)))
    print("Primera letra: " + (palabra[0]))
    print("Ultima letra: "+ (palabra[-1]))
    print("Repetida: " + str(palabra * 3))
    print("Decorada: " + "***" + palabra + "***")

#string_info()