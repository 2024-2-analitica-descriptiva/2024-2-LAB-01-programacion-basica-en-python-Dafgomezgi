"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('files\input\data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    data1 = [i.replace('\n','') for i in data]
    data1 = [i.split('\t') for i in data1]    
    a = [i[4].split(',') for i in data1]
    keys_list = [i[:3] for x in a for i in x]
    keys = sorted(set(keys_list))
    key = dict([(x, keys_list.count(x)) for x in keys])
        
    return key
