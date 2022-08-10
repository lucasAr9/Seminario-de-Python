import os
import csv
from collections import Counter


def todos_los_paises(datos):
    lista_paises = []
    for i in datos:
        lista_paises.extend(i[5].lower().split(','))
    paises = list(Counter(lista_paises))
    paises.sort()
    return paises


def un_anio_especifico(anio, datos):
    tit = [x[2] for x in datos if x[7] == anio and x[1] == 'TV Show']
    return tit


# def un_anio_especifico(anio, datos):
#     lista_pelis = []
#     for linea in datos:
#         if linea[7] == anio and linea[1] == 'TV Show':
#             lista_pelis.append(linea[2])
#     titulos = list(lista_pelis)
#     titulos.sort()
#     return titulos


nombre_carpeta = "archivos"
ruta_carpeta = os.path.join(os.getcwd(), '..', nombre_carpeta)
nombre_archivo = "netflix_titles.csv"
ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

archivo = open(ruta_completa, 'r', encoding='utf-8', newline='')

csv_reader = csv.reader(archivo, delimiter=',')

print(todos_los_paises(csv_reader))
print()

archivo.seek(0, 0)

anio = input('año a filtrar: ')
print(un_anio_especifico(anio, csv_reader))

archivo.close()
