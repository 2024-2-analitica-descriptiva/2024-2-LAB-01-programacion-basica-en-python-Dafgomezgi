"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

with open('data.csv', "r") as csv_file:
    data= csv_file.readlines()

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    
    
    """     
    fila_0 = [fila[0] for fila in data]
    lista_letras=[]
    for n in fila_0:
        if n not in lista_letras:
            lista_letras.append(n)

    lista_letras.sort()

    maximo=[]
    minimo=[]

    c=0
    a=[]

    for i in lista_letras:
        for b in data:
            if b[0] == lista_letras[c]:
                a.append(int(b[2]))

        minimo.append(min(a))
        maximo.append(max(a))
        c += 1
        a = []

    sln = list(zip(lista_letras,maximo, minimo))
    return sln






        


    


    



    



fila_0 = [fila[0] for fila in data]
lista_letras=[]
for n in fila_0:
    if n not in lista_letras:
        lista_letras.append(n)

lista_letras.sort()

maximo=[]
minimo=[]

c=0
a=[]

for i in lista_letras:
    for b in data:
        if b[0] == lista_letras[c]:
            a.append(int(b[2]))

    minimo.append(min(a))
    maximo.append(max(a))
    c += 1
    a = []

sln = list(zip(lista_letras,maximo, minimo))
print (sln)


