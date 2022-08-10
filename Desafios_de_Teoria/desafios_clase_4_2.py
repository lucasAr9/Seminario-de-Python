import os
import json
import csv

# Import the necessary packages
from consolemenu import ConsoleMenu, MenuFormatBuilder
from consolemenu.items import *


def imp_los_5():
    with open(archivo_los_5_paises, 'r', encoding='utf-8') as leer_achivo:
        paises = dict(json.load(leer_achivo))
    for pais in paises.items():
        print(pais)
    print("enter para volver al menu")
    input()


def imp_los_2021():
    with open(archivo_pelis_2021, 'r', encoding='utf-8') as leer_achivo:
        reader = csv.reader(leer_achivo, delimiter=',')
        for row in reader:
            print(row)
    print("enter para volver al menu")
    input()


# ruta de los archivos
carpeta_archivo = "archivos"
ruta_completa = os.path.join(os.getcwd(), carpeta_archivo)

archivo_pelis_2021 = os.path.join(ruta_completa, 'las_pelis_del_2021.csv')
archivo_los_5_paises = os.path.join(ruta_completa, 'los_5_paises.json')

# Create the menu
menu = ConsoleMenu("Catalogo de netflix")

# mostrar el archivo con los 5 paises con mas producciones
function_item = FunctionItem("ver los 5 paises con mas peliculas", imp_los_5)
# mostrar las peliculas del 2021
function_item_2 = FunctionItem("ver las pelicualas del 2021", imp_los_2021)

# mostrar el menu
menu.append_item(function_item)
menu.append_item(function_item_2)

menu.show()
