# -*- coding: utf-8 -*-
"""proyecto peliculas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pnBMxGzy6WjkGawcA2oH1Tv0QkHkdMum
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto
    pelicula={'nombre':nombre, 'genero':genero, 'duracion':duracion, 'anio':anio, 'clasificacion':clasificacion, 'hora':hora, 'dia':dia}

    return pelicula

#pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")

peli1 = crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
peli2 = crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")
peli3 = crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
peli4 = crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
peli5 = crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")


d={peli1['nombre']:peli1, peli2['nombre']:peli2, peli3['nombre']:peli3, peli4['nombre']:peli4, peli5['nombre']:peli5 }

print(d["Get Out"])
print(d["Shrek"])
print(d["Icarus"])
print(d["Inception"])
print(d["The Empire Strikes Back"])

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro.
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto
    d={p1['nombre']:p1, p2['nombre']:p2, p3['nombre']:p3, p4['nombre']:p4, p5['nombre']:p5}
    if nombre_pelicula not in d:
        return None

    return d[nombre_pelicula]

print(encontrar_pelicula('Hola', peli1, peli2, peli3, peli4, peli5))