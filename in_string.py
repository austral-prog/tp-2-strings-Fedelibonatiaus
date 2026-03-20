def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre= input("Ingrese su nombre: ")
    nombre_minuscula= (nombre.lower())


    print("Contiene a: " + str("a" in nombre_minuscula))
    print("Contiene e: " + str("e" in nombre_minuscula))
    print("Contiene i: " + str("i" in nombre_minuscula))
    print("Contiene o: " + str("o" in nombre_minuscula))
    print("Contiene u: " + str("u" in nombre_minuscula))


#check_vowels()