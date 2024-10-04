"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

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

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información inicializada."""
    return {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la película con el nombre dado entre las cinco películas proporcionadas."""
    for pelicula in [p1, p2, p3, p4, p5]:
        if pelicula["nombre"].lower() == nombre_pelicula.lower():
            return pelicula
    return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Devuelve la película con la mayor duración entre las cinco proporcionadas."""
    peliculas = [p1, p2, p3, p4, p5]
    pelicula_mas_larga = max(peliculas, key=lambda pelicula: pelicula["duracion"])
    return pelicula_mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duración promedio de las cinco películas y la devuelve en formato 'HH:MM'."""
    total_minutos = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    promedio_minutos = total_minutos // 5
    horas = promedio_minutos // 60
    minutos = promedio_minutos % 60
    return f"{horas:02}:{minutos:02}"


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las películas cuáles tienen un año de estreno posterior al año dado.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
        anio (int): Año límite para considerar la película como estreno.
    Retorna:
        str: Una cadena con los nombres de las películas estrenadas después del año dado.
             Si ninguna película coincide, retorna "Ninguna".
    """
    peliculas = [p1, p2, p3, p4, p5]
    estrenos = [pelicula["nombre"] for pelicula in peliculas if pelicula["anio"] > anio]

    if estrenos:
        return ", ".join(estrenos)
    else:
        return "Ninguna"


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuántas películas de clasificación '18+' hay entre las películas dadas.
    Parámetros:
        p1 (dict): Diccionario que contiene la información de la película 1.
        p2 (dict): Diccionario que contiene la información de la película 2.
        p3 (dict): Diccionario que contiene la información de la película 3.
        p4 (dict): Diccionario que contiene la información de la película 4.
        p5 (dict): Diccionario que contiene la información de la película 5.
    Retorna:
        int: El número de películas con clasificación '18+'.
    """
    peliculas = [p1, p2, p3, p4, p5]
    peliculas_18_mas = [pelicula for pelicula in peliculas if pelicula["clasificacion"] == '18+']

    return len(peliculas_18_mas)


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Verifica si es posible reagendar la película. 
    Para esto se verifica que no haya conflicto con el horario de otras películas y 
    si se debe controlar las preferencias de horario del usuario.
    
    Parámetros:
        peli (dict): Película a reagendar.
        nueva_hora (int): Nueva hora de la película (en formato de 24 horas).
        nuevo_dia (str): Nuevo día en el que se desea ver la película.
        control_horario (bool): Si se deben controlar las preferencias del usuario sobre el horario.
        p1, p2, p3, p4, p5 (dict): Diccionarios que contienen la información de las demás películas.
    
    Retorna:
        bool: True si se puede reagendar la película, False si no es posible.
    """
    peliculas = [p1, p2, p3, p4, p5]

    # Verificar si hay conflictos de horarios con otras películas
    for pelicula in peliculas:
        if pelicula != peli and pelicula["dia"] == nuevo_dia:
            hora_fin_peli = peli["hora"] + peli["duracion"]  # Hora de finalización de la película actual
            hora_fin_otra = pelicula["hora"] + pelicula["duracion"]  # Hora de finalización de la otra película

            # Comprobar superposición de horarios
            if not (nueva_hora >= hora_fin_otra or nueva_hora + peli["duracion"] <= pelicula["hora"]):
                print("No se puede reagendar la película. Hay un conflicto de horarios.")
                return False

    # Si se requiere control de horario, verificar restricciones
    if control_horario:
        # Restricción 1: No ver documentales después de las 10 PM
        if "Documental" in peli["genero"] and nueva_hora >= 2200:
            print("No se puede reagendar. No se permiten documentales después de las 10 PM.")
            return False
        # Restricción 2: No ver dramas los viernes
        if "Drama" in peli["genero"] and nuevo_dia.lower() == "viernes":
            print("No se puede reagendar. No se permiten dramas los viernes.")
            return False
        # Restricción 3: No ver películas entre semana a partir de las 11 PM o antes de las 6 AM
        if nuevo_dia.lower() in ["lunes", "martes", "miércoles", "jueves", "viernes"] and (nueva_hora >= 2300 or nueva_hora < 600):
            print("No se puede reagendar. No se permiten películas entre semana a partir de las 11 PM o antes de las 6 AM.")
            return False

    # Actualizar la película con el nuevo horario y día si no hay conflictos
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    print(f"La película '{peli['nombre']}' ha sido reagendada correctamente.")
    return True

    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parámetro a ver la película.
    Se verifica el cumplimiento de las restricciones de clasificación y edad.
    
    Parámetros:
        peli (dict): Película que se desea ver con el invitado.
        edad_invitado (int): Edad del invitado con quien se desea ver la película.
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorización de sus padres para ver la película.
    
    Retorna:
        bool: True si es posible invitar a la persona, False de lo contrario.
    """
    clasificacion = peli["clasificacion"]
    genero = peli["genero"]

    # Restricción 1: Si el invitado es mayor de edad (18 o más), puede ver cualquier película.
    if edad_invitado >= 18:
        return True

    # Restricción 2: No se puede invitar a personas menores de 15 años a ver películas de terror.
    if "Terror" in genero and edad_invitado < 15:
        print("No se puede invitar a una persona menor de 15 años a ver una película de Terror.")
        return False

    # Restricción 3: Si el invitado tiene 10 años o menos, solo se puede invitar a ver películas familiares.
    if edad_invitado <= 10 and "Familiar" not in genero:
        print("Solo se puede invitar a una persona de 10 años o menos a ver películas Familiares.")
        return False

    # Restricción 4: Verificar la clasificación por edad de la película (si necesita autorización de los padres).
    clasificacion_edad = {
        "todos": 0,
        "7+": 7,
        "13+": 13,
        "16+": 16,
        "18+": 18
    }

    # Si la clasificación de la película es mayor que la edad del invitado y no tiene autorización de los padres
    if clasificacion != "Documental" and edad_invitado < clasificacion_edad[clasificacion] and not autorizacion_padres:
        print("No se puede invitar al invitado sin autorización de los padres para ver esta película.")
        return False

    # Si todas las restricciones se cumplen, se puede invitar al invitado.
    return True










