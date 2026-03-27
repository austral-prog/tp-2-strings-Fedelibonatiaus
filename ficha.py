def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)



    Nombre= input("Ingresar Nombre Completo: ")
    Email= input("Ingresar Email: ")
    email_limpio= Email.lower().strip()
    nota1= input("Ingresar primera nota: ")
    nota2= input("Ingresar Segunda nota: ")
    nota3= input ("Ingresar tercera nota: ")

    print("="*24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print("Nombre: " + ((Nombre.strip().title())))
    print("Email: " + (email_limpio))
    #Iniciales
    Nombre_Limpio= ((Nombre.strip().title()))
    Nombre_Inicial= Nombre_Limpio[0]
    Espacio=Nombre_Limpio.find(" ")
    Apellido_Inicial= Nombre_Limpio[Espacio + 1]
    Iniciales= Nombre_Inicial + Apellido_Inicial
    print("Caracteres en nombre: " + str(len(Nombre_Limpio)))
    print("Iniciales: " + Iniciales)
    Onlynombre= Nombre_Limpio[:Espacio]
    Onlyapellido= Nombre_Limpio[Espacio + 1:]
    print("Usuario: " + (Onlyapellido + "." + Onlynombre).lower())
    arroba= "@" in email_limpio
    print("Email valido: " + str(arroba))
    # extraer dominio
    post_arroba = email_limpio.find("@")
    dominio = email_limpio[post_arroba + 1:]
    print("Dominio: " + (dominio))
    print("Nombre para archivo: " + str(Nombre_Limpio.replace(" ","_")))
    #contar a
    a_name= Nombre_Limpio.count("a")
    print("Cantidad de a: " + str(a_name))
    #codigo secreto
    secretcode= (Nombre_Limpio[::-1]).upper()
    print("Codigo secreto: " + str(secretcode))
    # Convertir notas
    n1 = int(nota1)
    n2 = int(nota2)
    n3 = int(nota3)

    # Operaciones matemáticas
    suma_notas = n1 + n2 + n3
    promedio = suma_notas / 3
    promedio_entero = suma_notas // 3

    print("Nota 1: " + str(n1))
    print("Nota 2: " + str(n2))
    print("Nota 3: " + str(n3))
    print("Suma: " + str(suma_notas))
    print("Promedio: " + str(promedio))
    print("Promedio entero: " + str(promedio_entero))
    print("="*24)


#ficha()
