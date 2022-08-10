import os
import csv
import pandas as pd


archivo_netflix = os.path.join(os.getcwd(), "netflix_titles.csv")
data_set = open(archivo_netflix, encoding='utf-8')

reader = csv.reader(data_set, delimiter=',')
shows_ar = filter(lambda x: x[5] == "Argentina" and x[1] == "TV Show", reader)

print('------------------------------como antes-----------------------------------------')
for elem in shows_ar:
    print(f"{elem[2]:<40} {elem[3]}")

print('------------------------------con pandas-----------------------------------------')
data_set = pd.read_csv(archivo_netflix, encoding='utf-8')
print(data_set)
