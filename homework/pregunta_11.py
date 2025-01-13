"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data1 = [i.replace('\n', ' ') for i in data]
    data1 = [i.split('\t') for i in data1]
    row_1 = [int(row[1]) for row in data1]
    row_3 = [row_3[3].split(',') for row_3 in data1]
    key_value = list(zip(row_3,row_1))
    
    keys = []
    for x in row_3:
        keys.extend(x)
    dict_keys = sorted(set(keys))
    
    dic=dict()
    for key in dict_keys:
        dic[key] = 0

    for x,y in key_value:
        for i in x:
            dic[i]+= y
        
    
    return dic
