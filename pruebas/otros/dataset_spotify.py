import os
import csv


def title_case(genero):
    """
    Función para cambiar los géneros de las canciones.
    :param genero: el género de la canción en string.
    :return: el género con title_case.
    """
    mayusculas = ['edm', 'dfw', 'uk', 'r&b', 'lgbtq+']
    titulo = map(lambda x: x.upper() if x in mayusculas else x.title(), genero.split(' '))
    return titulo


def recorrer_procesando(datos):
    """
    Función para recorrer el archivo csv de spotify.
    :param datos: los datos del csv reader.
    :return: la lista con los datos filtrados y con las columnas ordenadas.
    """
    datos_filt = []
    for linea in datos:
        # cambiar en nombre de genero a title_case
        linea[2] = title_case(linea[2])
        linea[2] = ' '.join(linea[2])
        # ordenar las columnas
        datos_filt.append([linea[2], linea[16], linea[3], linea[15], linea[5], linea[1]])
    return datos_filt


# ruta del archivo csv con los datos de spotify
nombre_archivo = "Spotify 2010 - 2019 Top 100.csv"
ruta_completa = os.path.join(nombre_archivo)

# ruta del nuevo archivo csv con los datos filtrados
nombre_nuevo = "dataset_spotify.csv"
nuevo_arch = os.path.join(nombre_nuevo)

try:
    with open(ruta_completa, 'r', encoding='utf-8') as spotify:
        csv_reader = csv.reader(spotify, delimiter=',')
        header_csv, datos_csv = next(csv_reader), list(csv_reader)
        datos_filtrados = recorrer_procesando(datos_csv)

    with open(nuevo_arch, 'w', encoding='utf-8', newline='') as columnas:
        csv_writer = csv.writer(columnas)
        csv_writer.writerow(['top genre', 'artist type', 'year released', 'top year', 'bpm', 'artist'])
        for linea in datos_filtrados:
            csv_writer.writerow(linea)
except FileNotFoundError:
    print('No se encontró el archivo "Spotify 2010 - 2019 Top 100.csv"')
