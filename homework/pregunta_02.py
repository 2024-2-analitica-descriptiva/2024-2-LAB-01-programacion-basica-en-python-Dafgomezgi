"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('files\input\data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    fila_0 = [fila[0] for fila in data]
    list_1 = []

    for n in fila_0:
        if n not in list_1:
         list_1.append(n)

    list_1.sort()

    lista_2=[]
    for n in list_1:
        lista_2.append(fila_0.count(n))

    List= list(zip(list_1,lista_2))

    return List

    




