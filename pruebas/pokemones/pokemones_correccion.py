import csv
import json
import os


def minor_attack_than_def(reader, minor_attack):
    for row in reader:
        if row[11] == '1' or row[11] == '2':
            if row[6] < row[7]:
                minor_attack.append({
                    "nombre": row[1],
                    "tipo": row[2],
                    "generacion": row[11],
                    "ataque": row[6],
                    "defensa": row[7]
                })


pokemones = "Pokemon.csv"
full_path = os.path.join(os.getcwd(), pokemones)
name_json = "resul_ataque_defen.json"
full_path_json = os.path.join(os.getcwd(), name_json)

# abrir el archivo csv para prosesar los datos de pokemones
try:
    file_pokemones = open(full_path, 'r', encoding='utf-8', newline='')
except FileNotFoundError:
    print("NO se encontro el archivo Pokemon.csv.")
    exit()
# archivo donde se guardan los resultados
file_json = open(full_path_json, 'w', encoding='utf-8', newline='')

reader = csv.reader(file_pokemones, delimiter=',')
minor_attack = []

minor_attack_than_def(reader, minor_attack)

json.dump(minor_attack, file_json, indent=4)

file_pokemones.close()
file_json.close()
