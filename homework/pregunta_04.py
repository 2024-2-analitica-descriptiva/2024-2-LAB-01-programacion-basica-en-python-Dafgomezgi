"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    data1= [i.replace('\n','') for i in data]
    data1 = [i.split('\t') for i in data]

    y=[] 

    for z in data1:
        y.append(z[2].split('-'))

    fila_0 = [fila[1] for fila in y]
   
    list_1 = sorted(set(fila_0))

    suma=[]
    C=0
    a=[]
    for p in list_1:
        for x in fila_0:
            if x == list_1[C]:
                a.append(1)
        suma.append(sum(a))
        a=[]
        C+=1

    resultado = list(zip(list_1, suma))
    return resultado


