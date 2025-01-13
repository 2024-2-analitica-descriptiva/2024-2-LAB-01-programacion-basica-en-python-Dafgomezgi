"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    fila_0 = [fila[0] for fila in data]
    fila_2 = [int(fila[2]) for fila in data]

    list_1 = sorted(set(fila_0))

    suma = []


    for x in list_1:  
        for i in range(len(fila_0)):
            total = sum(fila_2[i]  for i in range(len(fila_0)) if fila_0[i] == x)  
        suma.append(total)

    resultado = list(zip(list_1, suma))
    return resultado


