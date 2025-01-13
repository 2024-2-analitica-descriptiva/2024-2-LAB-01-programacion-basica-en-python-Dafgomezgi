"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
   pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data1 = open('data.csv', 'r').readlines()
    data1 = [i.replace('\n','') for i in data]
    data1 = [i.split('\t') for i in data]    
    a = [i[4].split(',') for i in data1]
    key_value = [(y[0:3], int(y[4:])) for x in a for y in x]
    keys = sorted(set(i[0] for i in key_value))

    values = []
    tupla = []
    for key in keys:
        for i in key_value:
            if i[0] == key:
                values.append(i[1])
        tupla.append((key, min(values), max(values)))
        values = []
        
    return tupla