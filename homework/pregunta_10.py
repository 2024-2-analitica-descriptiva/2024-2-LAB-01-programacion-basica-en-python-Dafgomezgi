"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data1 = [i.replace('\n','') for i in data]
    data1 = [i.split('\t') for i in data1]

    result = [
        (colum[0], len(colum[3].split(',')), len(colum[4].split(',')))
        for colum in data1
        ]   
    return result 
