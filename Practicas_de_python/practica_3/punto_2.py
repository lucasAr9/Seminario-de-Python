import os
import csv
import datetime
from collections import Counter

nombre_carpeta = "archivos"
ruta_carpeta = os.path.join(os.getcwd(), '..', nombre_carpeta)
nombre_archivo = "BBB_nuevo.csv"
ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

archivo = open(ruta_completa, 'r', encoding='utf-8', newline='')
csv_reader = csv.reader(archivo, delimiter=',')

dias_semana = ['lunes', 'martes', 'miercoles',
               'jueves', 'viernes', 'sabado', 'domingo'
               ]
formato = "%d/%m/%Y %H:%M"

header, datos_csv = next(csv_reader), list(csv_reader)

lista_grabaciones = []
primer_fecha = datetime.datetime.max
ultima_fecha = datetime.datetime.min

for linea in datos_csv:
    if linea[2] == 'Grabación vista':
        nro_dia = datetime.datetime.strptime(linea[0], formato).weekday()
        lista_grabaciones.append(dias_semana[nro_dia])

        fecha = datetime.datetime.strptime(linea[0], formato)
        if primer_fecha > fecha:
            primer_fecha = fecha
        if ultima_fecha < fecha:
            ultima_fecha = fecha

# el dia que mas vistas tuvo
dia_con_mas_vistas = Counter(lista_grabaciones).most_common(1)
print(dia_con_mas_vistas)

diferencia = ultima_fecha - primer_fecha
print('primer fecha: ' + str(primer_fecha))
print('ultima fecha: ' + str(ultima_fecha))
print('la diferencia entre la primer y ultima grav vista: ' + str(diferencia))

# Grabación vista
# ver que dia de la semana se ven mas gravaciones
# calcular cuantos dias pasaron entre la primer gravacion vista y la ultima
