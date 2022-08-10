import csv
import json


BBB_nuevo = open('BBB_nuevo.csv', 'r', encoding='utf-8', newline='')
reader_csv = csv.reader(BBB_nuevo, delimiter=',')

visualizaron_los_dos = open('visualizaron_los_dos.json', 'w')

nombre1 = []
nombre2 = []

for fila in reader_csv:
    if fila[2] == "Actividad BigBlueButtonBN visualizada":
        nombre1.append(fila[1])
    if fila[2] == "Grabación vista":
        nombre2.append(fila[1])

nombres1 = set(nombre1)
nombres2 = set(nombre2)
print('conjuntos--------------------------------------------------------------')
print(nombres1)
print(nombres2)

ambos = nombres1 & nombres2
print('interseccion de los conjuntos------------------------------------------')
print(ambos)

for i in ambos:
    json.dump(i, visualizaron_los_dos)

BBB_nuevo.close()
visualizaron_los_dos.close()
