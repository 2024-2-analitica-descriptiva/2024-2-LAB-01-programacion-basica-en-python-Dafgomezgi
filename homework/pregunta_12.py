"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('files\input\data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data1 = [i.replace('\n', ' ') for i in data]
    data1 = [i.split('\t') for i in data1]
    col1 = [row[0] for row in data]
    col5 = [row[4].split(',') for row in data1]
    key_value = list(zip(col1,col5))
    keys = sorted(set(col1))

    dic = dict()
    for key in keys:
        dic[key] = 0

    for x,y in key_value:
        for i in y:
            dic[x]+= int(i[4:])

    return dic