import os
import json
import csv
from collections import Counter


carpeta_archivo = "archivos"
ruta_completa = os.path.join(os.getcwd(), carpeta_archivo)

# ruta de los archivos
archivo_netflix = os.path.join(ruta_completa, "netflix_titles.csv")
archivo_peliculas_2021 = os.path.join(ruta_completa, 'las_pelis_del_2021.csv')
archivo_con_los_5_paises = os.path.join(ruta_completa, 'los_5_paises.json')

# archivo donde leer las peliculas
netflix_csv = open(archivo_netflix, 'r', encoding='utf-8', newline='')
reader_csv = csv.reader(netflix_csv, delimiter=',')

# archivo donde guardar las pelis del 2021
pelis_del_2021 = open(archivo_peliculas_2021, 'a', encoding='utf-8', newline='')
writer = csv.writer(pelis_del_2021, delimiter=',')

# guardar todos los paises que aparezcan
paises = []

for fila in reader_csv:
    if fila[7] == "2021":
        # escribir en el archivo de las peliculas del 2021
        writer.writerow(fila)
    if fila[5] != '':
        # guardar los paises
        paises.extend(fila[5].lower().replace(' ', '').split(','))

netflix_csv.close()
pelis_del_2021.close()

# escribir en un archivo json los 5 paises con mas peliculas
dict_de_los_paises = dict(Counter(paises).most_common(5))
los_5_paises = open(archivo_con_los_5_paises, 'w')
json.dump(dict_de_los_paises, los_5_paises, indent=4)

los_5_paises.close()
