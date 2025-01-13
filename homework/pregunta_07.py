"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]


    """

    data1 = [i.replace('\n','') for i in data]
    data1 = [i.split('\t') for i in data]
    colum1 =[]
    colum0 =[]
    for i in data1:
        colum0.append(i[0]) 
        colum1.append(i[1]) 

    lista1= sorted(set(colum1))

    lista1_int= [int(i) for i in lista1]


    comparacion=[]
    result=[]
    for i in lista1_int:
        comparacion=[]
        for z in data1:
            if int(z[1]) == lista1_int[i]:
                comparacion.append(z[0])
        result.append((i,comparacion))
    
    return result


