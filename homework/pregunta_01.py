"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('files\input\data.csv', "r") as csv_file:
        data= csv_file.readlines()


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
        
    suma_segunda_columna= sum(float(fila[2]) for fila in data)

    return suma_segunda_columna


