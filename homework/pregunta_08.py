"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """


    data1 = [i.replace('\n', '') for i in data]
    data1 = [i.split('\t') for i in data1]


    colum1 = [int(row[1]) for row in data1]
    colum0 = [row[0] for row in data1]


    lista1_int = sorted(set(colum1))


    result = []
    for i in lista1_int:
        comparacion = [row[0] for row in data1 if int(row[1]) == i]
        comparacion_orga = sorted(set(comparacion))
        result.append((i, comparacion_orga))

    return result