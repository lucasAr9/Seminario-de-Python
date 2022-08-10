import csv
import json
from os import path


def traducir_pos(pos):
    """Esta funcion retorna en pos, la traducion del ingles al español,
    de una determinada posicion. 
    Utilizando los datos de un archivo con las traducciones
    pos : Es el dato almacenado en la columna 'position' 
    de una determinada fila."""
    # Se almacena, en un diccionario, la traduccion (valor)
    # de la posicion (clave)
    try:
        ruta_completa = path.join(path.realpath(
            '.'), "datos_csv", "traducciones", "fifa_pos_ENG_ESP.json")

        with open(ruta_completa, 'r', encoding="utf-8") as traduccion:
            trad = json.load(traduccion)
            return trad[pos]
    except FileNotFoundError:
        return ("No encontrado")


def conversion_del_potencial(potencial):
    """Esta funcion retorna en potencial, su equivalenete en string
    potencial: es el valor de la columna 'Potential' de una determinada fila"""
    if(potencial < "60"):
        potencial = "Regular"
    elif(potencial > "60" and potencial <= "79"):
        potencial = "Bueno"
    elif(potencial > "79" and potencial <= "89"):
        potencial = "Muy bueno"
    else:
        potencial = "Sobresaliente"
    return potencial


def filtro_fifa(csvreader):
    """Esta funcion retorna en una lista las 
    lineas filtradas del csvreader de acuerdo al criterio adoptado"""
    lista_filtrada = []
    for ln in csvreader:
        # conversion de numero a strig segun el potencial
        ln[7] = conversion_del_potencial(ln[7])
        # traduccion de las posiciones
        # se aplica un split ya que, un jugador, puede tener varias posiciones
        ln[3] = '|'.join(
            list(map(lambda pos: traducir_pos(pos), ln[3].split('|'))))
        lista_filtrada.append(ln)

    return lista_filtrada


def reacomodar_columnas(lista_filtrada):
    """Esta funcion reacomoda las columnas de acuerdo al criterio elegido.
    lista_filtada: Es la lista retornada 
    por la funcion [filtro_fifa(csvreader)]"""
    # “Team”, “Nationality”, “Position”, “Age”, “Potential” y “Name”
    for ln in lista_filtrada:
        # a, b = b, a # Swapping
        ln[8], ln[0] = ln[0], ln[8]
        ln[2], ln[1] = ln[1], ln[2]
        ln[3], ln[2] = ln[2], ln[3]
        ln[5], ln[3] = ln[3], ln[5]
        ln[7], ln[4] = ln[4], ln[7]
        # name ya quedo en la posicion que le corresponde
    lista_filtrada = list(map(lambda ln: ln[0:6], lista_filtrada))
    return lista_filtrada


try:
    ruta_completa = path.join(path.realpath(
        '.'), "datos_csv", "FIFA-21 Complete.csv")
    with open(ruta_completa, 'r', encoding="utf-8") as fifa:
        csvreader = csv.reader(fifa, delimiter=';')
        next(csvreader)  # omito el encabezado
        lista_filtrada = filtro_fifa(csvreader)
        lista_filtrada = reacomodar_columnas(lista_filtrada)

    ruta_completa = path.join(path.realpath(
        '.'), "datos_csv", "fifa_21_filtrado.csv")
    with open(ruta_completa, 'w', encoding="utf-8") as fifa:
        writer = csv.writer(fifa)
        # Escribo el nuevo encabezado
        writer.writerow(["Team", "Nationality", "Position",
                        "Age", "Potential", "Name"])
        for ln in lista_filtrada:
            writer.writerow(ln)
except FileNotFoundError:
    print("Archivo csv 'FIFA-21 complete.csv' no encontrado")
