"""
Ejercicio nivel 2: Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la película.
    Parámetros:
        pelicula (dict): La película de la cual se van a mostrar los detalles.
        El diccionario que representa una película contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la película agendada.
            - genero (str): Géneros de la película separados por comas.
            - duracion (int): Duración en minutos de la película.
            - anio (int): Año de estreno de la película.
            - clasificacion (str): Clasificación de restricción por edad.
            - hora (int): Hora de inicio de la película (en formato de 24 horas, ej: 1430).
            - dia (str): Indica qué día de la semana se planea ver la película.
    """
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    print(f"Nombre: {nombre} - Año: {anio} - Duración: {duracion} mins")
    print(f"Género: {genero} - Clasificación: {clasificacion}")

    # Formatear la hora
    hora_formato = f"{hora // 100:02d}:{hora % 100:02d}"
    print(f"Día: {dia} - Hora: {hora_formato}")


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print("La película más larga es:")
    mostrar_informacion_pelicula(pelicula_mas_larga)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    duracion_promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print(f"La duración promedio de las películas es: {duracion_promedio}")


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de buscar películas de estreno.
    Esto es: las películas que sean más recientes que un año dado.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
    """
    try:
        anio = int(input("Ingrese el año a partir del cual desea buscar estrenos: "))
    except ValueError:
        print("Debe ingresar un número válido para el año.")
        return

    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)

    if estrenos == "Ninguna":
        print(f"No se encontraron películas estrenadas después del año {anio}.")
    else:
        print(f"Películas estrenadas después del año {anio}: {estrenos}")


def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de consultar cuántas películas de la agenda tienen clasificación 18+.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
    """
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print(f"Hay {cantidad} películas con clasificación 18+ en la agenda.")

    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de reagendar una película."""
    nombre = input("Ingrese el nombre de la película que desea reagendar: ").strip()
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    
    if pelicula is None:
        print(f"No se encontró ninguna película con el nombre '{nombre}'.")
        return
    
    try:
        nueva_hora = int(input("Ingrese la nueva hora (en formato 24 horas, ej: 1330): "))
        nuevo_dia = input("Ingrese el nuevo día de la semana (ej: Lunes): ").strip()
    except ValueError:
        print("Debe ingresar un formato válido para la hora.")
        return

    control_horario = input("¿Desea que se controlen sus preferencias de horario? (si/no): ").strip().lower()
    if control_horario == "si":
        control_horario = True
    elif control_horario == "no":
        control_horario = False
    else:
        print("Debe responder 'si' o 'no'.")
        return

    # Llamar a la función de reagendar y verificar si fue exitoso
    reagendado = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)

    if reagendado:
        print(f"La película '{nombre}' ha sido reagendada correctamente.")
    else:
        print(f"No se pudo reagendar la película '{nombre}'.")



def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de decidir si se puede invitar a alguien a ver una película.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
    """
    nom_peli = input("Ingrese el nombre de la película: ").strip()
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print(f"No se encontró ninguna película con el nombre '{nom_peli}'.")
        return

    try:
        edad_invitado = int(input("Ingrese la edad del invitado: "))
    except ValueError:
        print("Debe ingresar un número válido para la edad.")
        return

    autorizacion_padres = input("¿El invitado tiene autorización de los padres? (si/no): ").strip().lower()
    if autorizacion_padres == "si":
        autorizacion_padres = True
    elif autorizacion_padres == "no":
        autorizacion_padres = False
    else:
        print("Debe responder 'si' o 'no'.")
        return

    puede_invitar = mod.decidir_invitar(pelicula, edad_invitado, autorizacion_padres)

    if puede_invitar:
        print(f"Puedes invitar al invitado de {edad_invitado} años a ver '{nom_peli}'.")
    else:
        print(f"No puedes invitar al invitado de {edad_invitado} años a ver '{nom_peli}'.")

  
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
    Retorno:
        bool: True si el usuario selecciona una opción diferente a salir. 
              False si el usuario selecciona la opción para salir.
    """
    print("\nMenu de opciones")
    print("1 - Consultar película más larga")
    print("2 - Consultar duración promedio de las películas")
    print("3 - Consultar películas de estreno")
    print("4 - Consultar cuántas películas tienen clasificación 18+")
    print("5 - Reagendar película")
    print("6 - Verificar si se puede invitar a alguien")
    print("7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print(f"La opción '{opcion_elegida}' no es válida. Por favor, ingrese un número del 1 al 7.")

    return continuar_ejecutando



iniciar_aplicacion()
